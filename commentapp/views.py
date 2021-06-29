from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from rest_framework import generics, status
from .models import Post, Comment
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.views.generic.detail import DetailView

from .serializers import  PostSerializer, CommentSerializer
# Create your views here.

#add and create new posts
class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

#add and delete comments, add subcomment, delete all comments of a post
class CommentList(generics.ListCreateAPIView, APIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):

        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post_id', None)
        if post_id is not None:
            queryset = queryset.filter(post=post_id)
        return queryset
  
#delete comments related to a post id
    def delete(self, request, format=None):
        post_id = self.request.query_params.get('post_id', None)
        comment_delete =  Comment.objects.filter(post=post_id)
        if comment_delete and post_id:
            comment_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
#edit and delete single comments     
class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()




