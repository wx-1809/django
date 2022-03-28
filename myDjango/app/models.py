from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

class Test(models.Model):
     name = models.CharField(max_length=20)


class Artical(models.Model):
    title = models.CharField(max_length=100,verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    author = models.CharField(max_length=30,verbose_name='作者')
    time = models.DateTimeField(auto_now=True, verbose_name='时间')

    class Meta:
        verbose_name_plural = '文章'
        verbose_name: '文章'

class Comment(models.Model):
    articalid = models.IntegerField(verbose_name='文章id')
    user = models.CharField(max_length=30, verbose_name='ls评论人')
    content = models.CharField(max_length=100,verbose_name='评论内容')
    time = models.DateTimeField(auto_now=True, verbose_name='时间')

