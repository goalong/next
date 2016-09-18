from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=64, db_index=True, unique=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    intro = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tag'
        ordering = ['-created_time']


class Tag_Record(models.Model):
    tag = models.OneToOneField(Tag)
    creator = models.ForeignKey(User, related_name='tags')
    target_content_type = models.ForeignKey(ContentType, related_name='tag_target', blank=True, null=True)
    target_object_id = models.BigIntegerField(null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    created_time = models.DateTimeField(auto_now_add=True, editable=True, db_index=True)

    class Meta:
        db_table = 'tag_record'
        ordering = ['-created_time']
