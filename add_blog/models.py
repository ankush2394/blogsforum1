from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Blog(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    rating = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class rated_users_check(models.Model):

    rated_user = models.CharField(max_length=100)

    def __str__(self):
        return self.rated_user

class Comment(models.Model):

    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text