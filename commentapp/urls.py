from django.urls import path
from django.urls.conf import include
from .views import  PostList, CommentList, CommentUpdate
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='URL comments API')

urlpatterns = [

    # path('booklist/', BookList.as_view()),
    path('post/', PostList.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/update_delete/<int:pk>/', CommentUpdate.as_view()),
    # path('comment/update_delete/<int:post>/', CommentUpdate.as_view()),

    path('', schema_view),
    
   
]