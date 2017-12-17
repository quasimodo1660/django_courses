from __future__ import unicode_literals
from django.db import models

from ..user.models import *


class MessageManager(models.Manager):
    def message_validator(self,post):
        errors = {}
        if len(post['des'])<1:
            errors['des']='Message cannot be empty!'
        return errors

class CommentManager(models.Manager):
    def message_validator(self,post):
        errors = {}
        if len(post['des'])<1:
            errors['des']='Comment cannot be empty!'
        return errors


class Message(models.Model):
    content=models.TextField()
    user_id=models.ForeignKey(User,related_name='messages')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=MessageManager()
    
class Comment(models.Model):
    message_id=models.ForeignKey(Message,related_name='comments')
    content=models.TextField()
    user_id=models.ForeignKey(User,related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=CommentManager()