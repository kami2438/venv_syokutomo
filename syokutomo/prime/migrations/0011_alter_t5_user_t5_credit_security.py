# Generated by Django 3.2 on 2021-11-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0010_auto_20211125_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t5_user',
            name='t5_credit_security',
            field=models.CharField(max_length=3, null=True, verbose_name='セキュリティナンバー'),
        ),
    ]
