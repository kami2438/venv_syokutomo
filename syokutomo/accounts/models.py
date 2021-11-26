from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
from prime.models import T10_area
# Create your models here.
class CustomUser(AbstractUser):
    type_choice=(
        ("1", "ユーザー"),
        ("2", "店舗"),
        ("3", "配達員"))
    user_type=models.CharField(verbose_name='user_type',choices=type_choice,max_length=1,default="1")
    main_regist= models.BooleanField(default=False)
    area_id= models.ForeignKey(T10_area,verbose_name='エリア',on_delete= models.SET_DEFAULT,default='未設定')
    # nickname = models.CharField('ニックネーム', max_length=50,null=True)
    class Meta:
        verbose_name_plural="CustomUser"