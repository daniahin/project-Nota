from django.db import transaction
from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Tag, Comment
from apps.user.models import User
from config.settings import PAGE_NAMES


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': PAGE_NAMES['blog']}
    return render(request, 'blog/category/list.html', {'categories': blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    category = BlogCategory.objects.get(id=category_id)
    if category:
        breadcrumbs.update({'current': category})
    return render(request, 'blog/article/list.html', {'articles': articles, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    article = Article.objects.get(id=article_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): PAGE_NAMES['blog']}
    article_name = Article.objects.get(id=article_id)
    category_name = BlogCategory.objects.get(id=category_id)
    user = request.user
    comments = Comment.objects.filter(article=article, is_checked=True)
    error = None

    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article)
        if user.is_authenticated:
            data.update(user=user, name=user.first_name, email=user.email, is_checked=True)
        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/article/_created_comment.html', {'breadcrumbs': {'current': 'Коментар створено'}, 'back': request.path})
        else:
            error = form.errors
    else:
        form = CommentForm()

    if article_name:
        breadcrumbs.update({reverse('article_list', args=[category_id]): category_name})
    breadcrumbs.update({'current': article_name})
    return render(request, 'blog/article/view.html',
                  {'form': form, 'error': error, 'article': article, 'category': category,
                   'breadcrumbs': breadcrumbs, 'comments': comments})


def tag_search_article_list(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags__in=[tag_id])
    breadcrumbs = {'current': tag}
    return render(request, 'blog/article/tag_search.html', {'form': form, 'error': error, 'article': article,
                    'category': category, 'breadcrumbs': breadcrumbs, 'is_checked': is_checked})


# # @login_required
# def create_comment(request):
#     error = None
#     user = request.user
#     is_checked = Comment.is_checked
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             if user.is_authenticated:
#                 is_checked = True
#                 form = CommentForm(data={
#                     'first_name': user.first_name,
#                     'email': user.email,
#                 })
#             else:
#                 is_checked = False
#     else:
#         form = CommentForm()
#     return render(request, 'blog/article/_comment.html', {'form': form, 'is_checked': is_checked, 'error': error})
