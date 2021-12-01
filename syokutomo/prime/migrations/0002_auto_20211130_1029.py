# Generated by Django 3.2 on 2021-11-30 01:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t1_shop',
            name='t1_holiday',
        ),
        migrations.RemoveField(
            model_name='t7_delivery_man',
            name='t7_delivery_man_password',
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_fri',
            field=models.BooleanField(blank=True, null=True, verbose_name='金曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_mon',
            field=models.BooleanField(blank=True, null=True, verbose_name='月曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_sat',
            field=models.BooleanField(blank=True, null=True, verbose_name='土曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_sun',
            field=models.BooleanField(blank=True, null=True, verbose_name='日曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_tru',
            field=models.BooleanField(blank=True, null=True, verbose_name='木曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_tue',
            field=models.BooleanField(blank=True, null=True, verbose_name='火曜日'),
        ),
        migrations.AddField(
            model_name='t1_shop',
            name='t1_shop_wed',
            field=models.BooleanField(blank=True, null=True, verbose_name='水曜日'),
        ),
        migrations.AlterField(
            model_name='t1_shop',
            name='t1_bank_location',
            field=models.CharField(blank=True, max_length=3, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='支店番号'),
        ),
        migrations.AlterField(
            model_name='t1_shop',
            name='t1_bank_name',
            field=models.CharField(blank=True, max_length=4, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='金融機関名'),
        ),
        migrations.AlterField(
            model_name='t1_shop',
            name='t1_bank_number',
            field=models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='口座番号'),
        ),
        migrations.AlterField(
            model_name='t1_shop',
            name='t8_shop_category_id',
            field=models.ManyToManyField(max_length=4, to='prime.T8_shop_category', verbose_name='店舗カテゴリ'),
        ),
        migrations.AlterField(
            model_name='t2_order',
            name='t2_comment',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='コメント'),
        ),
        migrations.AlterField(
            model_name='t2_order',
            name='t5_user_id',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='prime.t5_user', verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='t4_food',
            name='t9_food_category_id',
            field=models.ManyToManyField(to='prime.T9_food_category', verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_bank_location',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='支店番号'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_bank_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='金融機関名'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_bank_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='口座番号'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_bank_password',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='口座暗証番号'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_charge_remain',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='チャージ残高'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_charge_tool',
            field=models.PositiveIntegerField(choices=[(1, '銀行'), (0, 'クレジットカード')], default=0, verbose_name='チャージ方法'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_credit_limit',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='有効期限'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_credit_number',
            field=models.CharField(blank=True, max_length=19, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], verbose_name='カード番号'),
        ),
        migrations.AlterField(
            model_name='t5_user',
            name='t5_credit_security',
            field=models.IntegerField(blank=True, null=True, verbose_name='セキュリティナンバー'),
        ),
    ]