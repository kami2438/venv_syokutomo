# Generated by Django 3.2 on 2022-01-13 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0007_remove_t12_charge_t12_charge_remain_ex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t4_food',
            name='t9_food_category_id',
        ),
        migrations.AddField(
            model_name='t4_food',
            name='t9_food_category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t9_food_category', verbose_name='カテゴリー'),
        ),
    ]
