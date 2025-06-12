from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment


# Serializer for user object (simplified fields)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Serializer for comment object
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'content',
            'created_at'
        ]


# Serializer for post object
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'category',
            'author',
            'created_at',
            'votes',
            'comments'
        ]
