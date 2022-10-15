from rest_framework import serializers
from .models import Post, Tag, Author


class AuthorOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]


class PostOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    tags = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    author = AuthorOutputSerializer()
