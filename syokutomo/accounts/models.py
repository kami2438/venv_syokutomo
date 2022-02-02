from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("sssssssssssssssssssssssssssssssssssssssssssssssssss")
# Create your models here.
class t10_area(models.Model):
   
    t10_area_prefecture=models.CharField(verbose_name='県',max_length=70,blank=False)
    t10_area_name=models.CharField(verbose_name='エリア名',max_length=70,blank=True,null=True)
    t10_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t10_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    def __str__(self):
        return " %s %s" % (self.t10_area_prefecture,self.t10_area_name)
class CustomUser(AbstractUser):
    type_choice=(
        ("1", "ユーザー"),
        ("2", "店舗"),
        ("3", "配達員"))
    user_type=models.CharField(verbose_name='user_type',choices=type_choice,max_length=1,default="1")
    main_regist= models.BooleanField(default=False)
    address=models.CharField(verbose_name='詳細住所',default="",max_length=100)
    area= models.ForeignKey(t10_area,verbose_name='エリア',on_delete= models.CASCADE ,default="2359")
    # nickname = models.CharField('ニックネーム', max_length=50,null=True)
    class Meta:
        verbose_name_plural="CustomUser"