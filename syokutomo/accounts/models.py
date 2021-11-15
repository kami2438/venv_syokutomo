from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    type_choice=(
        ("1", "ユーザー"),
        ("2", "店舗"),
        ("3", "配達員"))
    user_type=models.IntegerField(verbose_name='user_type',choices=type_choice)
    class Meta:
        verbose_name_plural="CustomUser"