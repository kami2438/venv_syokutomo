# Generated by Django 3.2 on 2021-11-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0011_alter_t5_user_t5_credit_security'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t5_user',
            name='t5_credit_security',
            field=models.CharField(max_length=6, null=True, verbose_name='セキュリティナンバー'),
        ),
    ]