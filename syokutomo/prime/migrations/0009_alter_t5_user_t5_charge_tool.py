# Generated by Django 3.2 on 2021-11-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0008_alter_t5_user_t10_area_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t5_user',
            name='t5_charge_tool',
            field=models.PositiveIntegerField(choices=[(1, '銀行'), (0, 'クレジットカード')], default=0, null=True, verbose_name='チャージ方法'),
        ),
    ]