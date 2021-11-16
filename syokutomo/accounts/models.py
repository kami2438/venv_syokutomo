from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.
class CustomUser(AbstractUser):
    type_choice=(
        ("1", "ユーザー"),
        ("2", "店舗"),
        ("3", "配達員"))
    user_type=models.CharField(verbose_name='user_type',choices=type_choice,max_length=1,default="1")
    main_regist= models.BooleanField(default=False)
    # nickname = models.CharField('ニックネーム', max_length=50,null=True)
    class Meta:
        verbose_name_plural="CustomUser"