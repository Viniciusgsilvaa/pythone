from django.views.generic import TemplateView
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer 

"""
V1
"""
class PostApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsApiView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Post.objects.all()
   serializer_class = PostSerializer