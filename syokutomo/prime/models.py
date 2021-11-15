from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


# number_only=RegexValidator(regex='^[0-9]{1,}]$', message='数字だけ入力ください')

class T1_shop(models.Model):
    t1_shop_id = models.CharField(verbose_name='店舗ID',null=False,primary_key= true,max_length=10, validators=[RegexValidator(regex=r"^S[0-9]*$")])
    t1_shop_name_prime = models.CharField(verbos_name= '店名',max_length=3,null=False)
    t1_area_id= models.ForeignKey(T10_area,verbose_name='エリアID',on_delete=models.CASCADE)
    t1_address= models.CharField(verbos_name= '住所',max_length=200,null=False)
    t1_shop_category_id= models.ForeignKey(verbose_name='店舗カテゴリーID',max_length=4,on_delete=models.CASCADE)
    t1_holiday=models.IBinaryField(verbose_name='定休日',max_length=7,blank=True)
    t1_start_time=models.DateTimeField(verbose_name='注文開始時間',null=False)
    t1_end_time=models.DateTimeField(verbose_name='注文終了時間',null=False)
    t1_favorite_count=models.IntegerField(verbose_name='お気に入り数',null=False,default=0,max_length=7)
    t1_tel_number=models.PositiveIntegerField(verbose_name='電話番号',null=False,max_length=11)
    t1_shop_discribe=models.TextField(verbose_name='説明',max_length=200)
    t1_shop_name_sub= models.CharField(verbose_name='サブ店名',null=true,max_length=30)
    t1_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t1_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t1_mail=models.EmailField(verbose_name='メールアドレス',max_length=90,null=False)
    t1_password=models.CharField(verbose_name='パスワード',max_length=20,null=False,default='123')
    t1_bank_name=models.CharField(verbose_name='金融機関名',null=False,max_length=4,blank=False, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_location=models.CharField(verbose_name='支店番号',null=False,max_length=3,blank=False, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_number=models.CharField(verbose_name='口座番号',null=False,max_length=6,blank=False, validators=[RegexValidator(regex=r"^[0-9]*$")])

class t2_order(models.Model):
    t2_order_id= models.CharField(verbose_name='注文ID',primary_key=True,max_length=15, validators=[RegexValidator(regex=r"^O[0-9]*$")])
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',max_length=10,validators=[RegexValidator(regex=r"^S[0-9]*$")],on_delete=models.CASCADE,null=False)
    t5_user_id=models.ForeignKey(t5_user,verbose_name='ユーザーID',max_length=10,validators=[RegexValidator(regex=r"^U[0-9]*$")],null=False,on_delete=models.CASCADE )
    t2_comment=models.TextField(verbose_name='コメント',max_length=500)
    t2_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t2_update_at=models.DateTimeField(verbose_name='作成日時')
    t2_week=(verbose_name='')
    t2_order_count=(verbose_name='')