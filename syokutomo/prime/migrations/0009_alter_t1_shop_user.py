# Generated by Django 3.2 on 2022-01-18 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prime', '0008_auto_20220113_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t1_shop',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]