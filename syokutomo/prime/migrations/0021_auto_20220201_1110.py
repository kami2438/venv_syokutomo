# Generated by Django 3.2 on 2022-02-01 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0020_alter_t3_order_detail_t3_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t3_order_detail',
            name='t3_order_deliver_status',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='配送状態'),
        ),
        migrations.AlterField(
            model_name='t3_order_detail',
            name='t3_review_done',
            field=models.BooleanField(blank=True, default=False, verbose_name='レビューしたか'),
        ),
    ]
