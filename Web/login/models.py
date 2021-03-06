from distutils.command.upload import upload
import email
from email import message

from django.db import models


class login(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class comment(models.Model):
    author = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    photo = models.ImageField(upload_to = "img/%Y/%m/%d/")  
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.author
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class pacage(models.Model):
    states = models.CharField(max_length=255)
    day_2go = models.CharField(max_length=255)


class basket(models.Model):
    S_NAME = models.CharField(max_length=255)

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    messege = models.TextField(blank=True)
