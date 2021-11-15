from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

# Create your models here.


# number_only=RegexValidator(regex='^[0-9]{1,}]$', message='数字だけ入力ください')

class T1_shop(models.Model):
    t1_shop_id = models.CharField(verbose_name='店舗ID',null=False,primary_key= true,max_length=10, validators=[RegexValidator(regex=r"^S[0-9]*$")])
    t1_shop_name_prime = models.CharField(verbos_name= '店名',max_length=3,null=False)
    t1_area_id= models.ForeignKey(T10_area,verbose_name='エリアID',on_delete=models.CASCADE)
    t1_address= models.CharField(verbos_name= '住所',max_length=200,null=False)
    t1_shop_category_id= models.ForeignKey(verbose_name='店舗カテゴリーID',max_length=4,on_delete=models.CASCADE)
    t1_holiday=models.CharField(verbose_name='定休日',max_length=7,blank=True,validators=[RegexValidator(regex=r"^[0-1]\{7\}$")])
    t1_start_time=models.DateTimeField(verbose_name='注文開始時間',null=False)
    t1_end_time=models.DateTimeField(verbose_name='注文終了時間',null=False)
    t1_favorite_count=models.IntegerField(verbose_name='お気に入り数',null=False,default=0,max_length=7)
    t1_tel_number=models.PositiveIntegerField(verbose_name='電話番号',null=False,max_length=11,blank=True)
    t1_shop_discribe=models.TextField(verbose_name='説明',max_length=200,blank=True)
    t1_shop_name_sub= models.CharField(verbose_name='サブ店名',null=true,max_length=30,blank=True)
    t1_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t1_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t1_mail=models.EmailField(verbose_name='メールアドレス',max_length=90,null=False)
    t1_password=models.CharField(verbose_name='パスワード',max_length=20,null=False,default='123')
    t1_bank_name=models.CharField(verbose_name='金融機関名',null=False,max_length=4, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_location=models.CharField(verbose_name='支店番号',null=False,max_length=3, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_number=models.CharField(verbose_name='口座番号',null=False,max_length=6,validators=[RegexValidator(regex=r"^[0-9]*$")])
class T2_order(models.Model):
    t2_order_id= models.CharField(verbose_name='注文ID',primary_key=True,max_length=15, validators=[RegexValidator(regex=r"^O[0-9]*$")])
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',max_length=10,on_delete=models.CASCADE,null=False)
    t5_user_id=models.ForeignKey(T5_user,verbose_name='ユーザーID',max_length=10,null=False,on_delete=models.CASCADE )
    t2_comment=models.TextField(verbose_name='コメント',max_length=500,blank=True)
    t2_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t2_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t2_week=models.PositiveIntegerField(verbose_name='曜日',max_length=1,blank=True)
    t2_order_count=PositiveIntegerField(verbose_name='残り回数',null=False,max_length=4)
class T3_order_detail(models.Model):
    t3_order_detail_id=models.CharField(verbose_name='注文詳細ID',primary_key=True,max_length=20, validators=[RegexValidator(regex=r"^OD[0-9]*$")])
    t2_order_id=models.ForeignKey(T2_order,verbose_name='注文ID',null=False,on_delete=models.CASCADE )
    t4_food_id=models.ForeignKey(T4_food_id,verbose_name='料理ID',on_delete=models.CASCADE ,null=False)
    t3_amount=models.PositiveIntegerField(verbose_name='数量',default=1,null=False)
    t3_delivery_date=models.DateTimeField(verbose_name='配達予定時刻' ,null=False)
    t3_comment=models.TextField(verbose_name='コメント',max_length=500,blank=True)
    t3_payment=PositiveIntegerField(verbose_name='料金',max_length=8,null=False )
    t3_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t3_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t7_delivery_man_id=models.ForeignKey(T7_delivery_man,verbose_name='配達員ID',on_delete=models.CASCADE )
    t3_order_deliver_status=PositiveIntegerField(verbose_name='配送状態',null=False,max_length=1)
class T4_food(models.Model):
    t4_food_id=models.CharField(verbose_name='料理ID',Prinary_key=True,max_length=15,validators=[RegexValidator(regex=r"^F[0-9]*$")])
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',max_length=10,on_delete=models.CASCADE,null=False)
    t9_food_category_id=models.ForeignKey(T9_food_category,verbose_name='カテゴリーID',on_delete=models.CASCADE,null=False)
    # postgresql specific model fields
    t4_ingredients=ArrayField(models.CharField(max_length=300), blank=True,verbose_name='食材')

    t4_price=models.PositiveIntegerField(verbose_name='単価',max_length=7,null=False,blank=False)
    t4_food_name=models.CharField(verbose_name='料理名',max_length=40,null=False,blank=False)
    t4_food_discribe=models.TextField(verbose_name='説明',max_length=400,blank=True)
    t4_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t4_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t4_order_count=models.PositiveIntegerField(verbose_name='注文回数',max_length=10,blank=True)
class T5_user(models.Model):