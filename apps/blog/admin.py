from django.contrib import admin
from apps.blog.models import Article, BlogCategory, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from apps.user.models import User

admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_list_link']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']


    def article_list_link(self, obj):
        count = Article.objects.filter(category=obj).count()
        url = (
            reverse('admin:blog_article_changelist')
            + '?'
            + urlencode({'category__id': obj.id, 'category__id__exact': obj.id})
        )
        return format_html(f'<a href="{url}">Cтатті(ей): {count}</a>')

    article_list_link.short_description = 'Статті'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag_thumbnail', 'category_link', 'tags_links', 'created_at', 'user']
    list_display_links = ['id', 'title', 'user']
    fields = ['category', 'image_tag', 'image', 'tags', 'title', 'text_preview', 'text', 'user']
    readonly_fields = ['image_tag']
    list_filter = ['category', 'tags']

    def category_link(self, obj):
        if obj.category:
            url = reverse('admin:blog_blogcategory_change', args=[obj.category.id])
            return format_html(f'<a href="{url}">{obj.category.name}</a>')

    category_link.short_description = 'Категорія'

    def tags_links(self, obj):
        tags_links = []
        for tag in obj.tags.all():
            url = reverse('admin:blog_tag_change', args=[tag.id])
            tags_links.append(f'<a href="{url}">#{tag.name}</a>')

        return format_html(', '.join(tags_links))
    tags_links.short_description = 'Теги'

    def user_link(self, obj):
        if obj.user:
            url = reverse('admin:user_user_change', args=[obj.user.id])
            return format_html(f'<a href="{url}">{obj.user.name}</a>')

    user_link.short_description = 'Користувач'