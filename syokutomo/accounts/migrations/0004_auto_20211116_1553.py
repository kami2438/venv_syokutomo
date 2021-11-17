# Generated by Django 3.2 on 2021-11-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='nickname',
        ),
        migrations.AddField(
            model_name='customuser',
            name='main_regist',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'ユーザー'), ('2', '店舗'), ('3', '配達員')], default='1', max_length=1, verbose_name='user_type'),
        ),
    ]