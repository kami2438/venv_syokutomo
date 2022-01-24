# Generated by Django 3.2 on 2022-01-24 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prime', '0012_auto_20220124_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t2_order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
