# Generated by Django 3.2 on 2021-12-02 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0002_t1_shop_t8_shop_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t11_love',
            name='t1_shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t1_shop', verbose_name='店舗ID'),
        ),
        migrations.AlterField(
            model_name='t11_love',
            name='t5_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t5_user', verbose_name='ユーザーID'),
        ),
        migrations.AlterField(
            model_name='t12_charge',
            name='t5_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t5_user', verbose_name='店舗ID'),
        ),
        migrations.AlterField(
            model_name='t1_shop',
            name='t1_bank_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='金融機関名'),
        ),
        migrations.AlterField(
            model_name='t2_order',
            name='t1_shop_id',
            field=models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t1_shop', verbose_name='店舗ID'),
        ),
        migrations.AlterField(
            model_name='t2_order',
            name='t5_user_id',
            field=models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t5_user', verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='t3_order_detail',
            name='t2_order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t2_order', verbose_name='注文ID'),
        ),
        migrations.AlterField(
            model_name='t3_order_detail',
            name='t4_food_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t4_food', verbose_name='料理ID'),
        ),
        migrations.AlterField(
            model_name='t4_food',
            name='t1_shop_id',
            field=models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t1_shop', verbose_name='店舗ID'),
        ),
        migrations.AlterField(
            model_name='t6_review',
            name='t1_shop_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prime.t1_shop', verbose_name='ユーザーID'),
        ),
    ]
