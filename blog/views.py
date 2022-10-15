from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Post, Author, Tag
from .serializers import PostOutputSerializer

# Create your views here.


class CreateListPosts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostOutputSerializer(posts, many=True)
        return Response(serializer.data)
