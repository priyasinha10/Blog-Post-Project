from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'content',
            'published_date',
            'author',
            'author_username',
            'image'
        ]
        read_only_fields = ['author', 'published_date']
