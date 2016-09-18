from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts")
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.IntegerField()   #Todo

    class Meta:
        db_table = 'post'
        ordering = ['-created_time']

class Post_Vote(models.Model):
    from_user = models.ForeignKey(User, related_name="post_votes")
    post = models.ForeignKey(Post, related_name="votes")
    value = models.IntegerField(choices=[(-1, -1), (0, 0), (1, 1)])
    created_time = models.DateTimeField(auto_now_add=True, db_index=True, null=True)

    class Meta:
        db_table = 'post_vote'
        ordering = ['-created_time']

class Post_Comment(models.Model):
    from_user = models.ForeignKey(User, related_name="comments")
    post = models.ForeignKey(Post, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    content = models.CharField(max_length=255)
    reply_to = models.ForeignKey('self', null=True, blank=True)
    status = models.IntegerField()  # Todo

    class Meta:
        db_table = 'post_comment'
        ordering = ['-created_time']