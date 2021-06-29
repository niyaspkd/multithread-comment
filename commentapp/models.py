from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
  
    def __str__(self):
        return f'{self.author.username}\'s Post- {self.title}'
  
 #main comment used to add subcomment 
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    main_comment = models.ForeignKey('self', blank=True, null=True, related_name='subcomment', on_delete=models.CASCADE)

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

