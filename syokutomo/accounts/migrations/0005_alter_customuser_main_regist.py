# Generated by Django 3.2 on 2021-11-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211116_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='main_regist',
            field=models.BooleanField(default=False),
        ),
    ]
