from django.db import models
from django.conf import settings
from django.forms import CharField


# Create your models here.
class Article(models.Model):
    nickname = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField()
    password = models.CharField(max_length=100)
    # article_img = models.ImageField()
    article_image = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
            return self.nickname



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    nickname = CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100)

    def __str__(self):
            return self.content
