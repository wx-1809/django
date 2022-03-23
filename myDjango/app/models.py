from django.db import models

# Create your models here.
# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     age = models.IntegerField()

class Test(models.Model):
    name = models.CharField(max_length=20)

