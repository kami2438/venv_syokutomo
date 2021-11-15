from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    type_choice=(
        ("1", "ユーザー"),
        ("2", "店舗"),
        ("3", "配達員"))
    user_type=models.CharField(verbose_name='user_type',choices=type_choice　max_length=1)
    class Meta:
        verbose_name_plural="CustomUser"