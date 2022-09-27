from rest_framework import serializers
from apps.blog.models import Article, Tag, BlogCategory


class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )
