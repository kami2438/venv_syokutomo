# Generated by Django 3.2 on 2022-01-24 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0010_alter_t2_order_t1_shop_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t2_order',
            name='t5_user_id',
        ),
    ]