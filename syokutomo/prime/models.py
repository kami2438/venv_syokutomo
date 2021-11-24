from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser


from django.core.validators import RegexValidator, MaxValueValidator ,MinValueValidator
from import_export import resources
# Create your models here.


# number_only=RegexValidator(regex='^[0-9]{1,}]$', message='数字だけ入力ください')

#foreign key 先のクラスを先に初期化
class T10_area(models.Model):
   
    t10_area_prefecture=models.CharField(verbose_name='県',max_length=70,blank=False)
    t10_area_name=models.CharField(verbose_name='エリア名',max_length=70,blank=True,null=True)
    t10_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t10_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    def __str__(self):
        return " %s " % (self.id)

class T8_shop_category(models.Model):
 
    t8_shop_category_name=models.CharField(verbose_name='カテゴリ名',max_length=40,blank=True,null=False)
    t8_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t8_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    # def __str__(self):
    #     return "%s " % (self.id)

class T1_shop(models.Model):
    #ユーザー別foreignkey
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
 
  

    t1_shop_name_prime = models.CharField(verbose_name= '店名',max_length=3,null=False)
    t10_area_id= models.ForeignKey(T10_area,verbose_name='エリアID',on_delete= models.SET_DEFAULT,default='未設定')
    t1_address= models.CharField(verbose_name= '住所',max_length=200,null=False)
    t8_shop_category_id= models.ManyToManyField(T8_shop_category,verbose_name='店舗カテゴリID',max_length=4)
    t1_holiday=models.CharField(verbose_name='定休日',max_length=7,null=True,validators=[RegexValidator(regex=r"^[0-1]\{7\}$")])
    t1_start_time=models.DateTimeField(verbose_name='注文開始時間',null=False)
    t1_end_time=models.DateTimeField(verbose_name='注文終了時間',null=False)
    t1_favorite_count=models.IntegerField(verbose_name='お気に入り数',null=False,default=0)
    t1_tel_number=models.CharField(verbose_name='電話番号',max_length=11,validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_shop_discribe=models.TextField(verbose_name='説明',max_length=200,blank=True,null=True)
    t1_shop_name_sub= models.CharField(verbose_name='サブ店名',max_length=30,blank=True,null=True)
    t1_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t1_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)

    t1_shop_photo_01=models.ImageField(verbose_name='写真01',blank=True,null=True)
    t1_shop_photo_02=models.ImageField(verbose_name='写真02',blank=True,null=True)
    t1_shop_photo_03=models.ImageField(verbose_name='写真03',blank=True,null=True)
    t1_shop_photo_04=models.ImageField(verbose_name='写真04',blank=True,null=True)
    t1_shop_photo_05=models.ImageField(verbose_name='写真05',blank=True,null=True)
    
    t1_bank_name=models.CharField(verbose_name='金融機関名',null=False,max_length=4, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_location=models.CharField(verbose_name='支店番号',null=False,max_length=3, validators=[RegexValidator(regex=r"^[0-9]*$")])
    t1_bank_number=models.CharField(verbose_name='口座番号',null=False,max_length=6,validators=[RegexValidator(regex=r"^[0-9]*$")])
    # def __str__(self):
    #     return "%s " % (self.id)

class T9_food_category(models.Model):
 

    t9_shop_category_name=models.CharField(verbose_name='カテゴリ名',max_length=40,blank=True,null=False)
    t9_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t9_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)

class T4_food(models.Model):
 
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',max_length=10,on_delete=models.CASCADE,null=False)
    t9_food_category_id=models.ManyToManyField(T9_food_category,verbose_name='カテゴリーID')
    # postgresql specific model fields
    t4_ingredients=ArrayField(models.CharField(max_length=300), blank=True,verbose_name='食材',null=True)

    t4_food_photo_01=models.ImageField(verbose_name='写真01',blank=True,null=True)

    t4_price=models.PositiveIntegerField(verbose_name='単価',null=False,blank=False)
    t4_food_name=models.CharField(verbose_name='料理名',max_length=40,null=False,blank=False)
    t4_food_discribe=models.TextField(verbose_name='説明',max_length=400,blank=True,null=True)
    t4_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t4_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t4_order_count=models.PositiveIntegerField(verbose_name='注文回数',blank=True,null=True)
    # def __str__(self):
    #     return "%s " % (self.id)

class T5_user(models.Model):
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)


    # t5_user_id=models.CharField(verbose_name='ユーザーID',primary_key=True,max_length=15,validators=[RegexValidator(regex=r"^U[0-9]*$")])

    t5_user_firstname=models.CharField(verbose_name='顧客姓',max_length=30,blank=False)
    t5_user_lastname=models.CharField(verbose_name='顧客名',max_length=30,blank=False)
    t10_area_id=models.ForeignKey(T10_area,verbose_name='エリアID',null=False,on_delete=models.SET_DEFAULT,default='エリアID未設定')
    t5_address=models.CharField(verbose_name='住所',max_length=70)
    t5_post=models.CharField(verbose_name='郵便番号',max_length=7,validators=[RegexValidator(regex=r"^F[0-9]*$")])
    t5_tel_number=models.CharField(verbose_name='電話番号',max_length=11,validators=[RegexValidator(regex=r"^F[0-9]*$")])
    t5_landmark=models.TextField(verbose_name='自宅の目印',max_length=200,blank=True,null=True)
    t5_allergy=ArrayField(models.TextField(max_length=300),verbose_name='控えるべき食材',blank=True,null=True)
    t5_charge_tool=models.PositiveIntegerField(verbose_name='チャージ方法',validators=[MaxValueValidator(1)],default=0,null=True)
    t5_charge_remain=models.IntegerField(verbose_name='チャージ残高',default=0,null=True)
    t5_credit_number=models.CharField(verbose_name='カード番号',max_length=19,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t5_credit_limit=models.CharField(verbose_name='有効期限',max_length=4,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t5_credit_security=models.PositiveIntegerField(verbose_name='セキュリティナンバー',null=True,validators=[MaxValueValidator(999)])
    t5_bank_name=models.CharField(verbose_name='金融機関名',max_length=8,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t5_bank_location=models.CharField(verbose_name='支店番号',max_length=8,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t5_bank_number=models.CharField(verbose_name='口座番号',max_length=10,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t5_bank_password=models.CharField(verbose_name='口座暗証番号',max_length=4,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    # def __str__(self):
    #     return "%s " % (self.id)


class T2_order(models.Model):
    # t2_order_id= models.CharField(verbose_name='注文ID',primary_key=True,max_length=15, validators=[RegexValidator(regex=r"^O[0-9]*$")])
 
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',max_length=10,on_delete=models.CASCADE,null=False)
    t5_user_id=models.ForeignKey(T5_user,verbose_name='ユーザーID',max_length=10,null=False,on_delete=models.CASCADE )
    t2_comment=models.TextField(verbose_name='コメント',max_length=500,blank=True)
    t2_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t2_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t2_week=models.PositiveIntegerField(verbose_name='曜日',blank=True,null=True,validators=[MaxValueValidator(7)])
    t2_order_count=models.PositiveIntegerField(verbose_name='残り回数',null=False)
class T7_delivery_man(models.Model):
    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
 
    

    # t7_delivery_man_id=models.CharField(verbose_name='配達員ID',primary_key=True,max_length=10,validators=[RegexValidator(regex=r"^D[0-9]*$")])
  
    t7_delivery_man_firstname=models.CharField(verbose_name='姓',max_length=20)
    t7_delivery_man_lastname=models.CharField(verbose_name='名',max_length=20)
    t7_delivery_man_tel=models.CharField(verbose_name='電話番号',max_length=11,validators=[RegexValidator(regex=r"^[0-9]*$")])
    # t7_delivery_man_mail=models.EmailField(verbose_name='メールアドレス',max_length=90,blank=False)
    t10_area_id=models.ForeignKey(T10_area,verbose_name='エリアID',on_delete= models.SET_DEFAULT,default='未設定')
    t7_delivery_man_password=models.CharField(verbose_name='パスワード',max_length=20,blank=False)
    t7_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t7_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t7_bank_name=models.CharField(verbose_name='金融機関名',max_length=8,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t7_bank_location=models.CharField(verbose_name='支店番号',max_length=8,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    t7_bank_number=models.CharField(verbose_name='口座番号',max_length=10,validators=[RegexValidator(regex=r"^[0-9]*$")],null=True)
    def __str__(self):
        return "%s " % (self.id)



class T3_order_detail(models.Model):
    # t3_order_detail_id=models.CharField(verbose_name='注文詳細ID',primary_key=True,max_length=20, validators=[RegexValidator(regex=r"^OD[0-9]*$")])

    t2_order_id=models.ForeignKey(T2_order,verbose_name='注文ID',null=False,on_delete=models.CASCADE )
    t4_food_id=models.ForeignKey(T4_food,verbose_name='料理ID',on_delete=models.CASCADE ,null=False)
    t3_amount=models.PositiveIntegerField(verbose_name='数量',default=1,null=False)
    t3_delivery_date=models.DateTimeField(verbose_name='配達予定時刻' ,null=False)
    t3_comment=models.TextField(verbose_name='コメント',max_length=500,blank=True,null=True)
    t3_payment=models.PositiveIntegerField(verbose_name='料金',null=False )
    t3_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t3_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t7_delivery_man_id=models.ForeignKey(T7_delivery_man,verbose_name='配達員ID',on_delete=models.CASCADE )
    t3_order_deliver_status=models.PositiveIntegerField(verbose_name='配送状態',null=False,validators=[MaxValueValidator(1)])


class T6_review(models.Model):
    # t6_review_id=models.CharField(verbose_name='レビューID',primary_key=True,max_length=15,validators=[RegexValidator(regex=r"^R[0-9]*$")])
   
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='ユーザーID',on_delete=models.CASCADE,null=False)
    t6_star=models.PositiveSmallIntegerField(verbose_name='星',validators=[MaxValueValidator(5),MinValueValidator(1)])
    t6_title=models.CharField(verbose_name='タイトル',max_length=40,null=True,blank=True)
    t6_sentence=models.TextField(verbose_name='本文',max_length=400,null=True,blank=True)
    t6_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t4_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)

class T11_love(models.Model):
    # t11_love_id=models.CharField(verbose_name='お気に入りID',primary_key=True,max_length=20,validators=[RegexValidator(regex=r"^L[0-9]*$")])
    # id=models.AutoField(primary_key=True)
    t1_shop_id=models.ForeignKey(T1_shop,verbose_name='店舗ID',on_delete=models.CASCADE,null=False)
    t5_user_id=models.ForeignKey(T5_user,verbose_name='ユーザーID',on_delete=models.CASCADE,null=False)
    t11_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t11_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
class T12_charge(models.Model):
    # t12_charge_id=models.CharField(verbose_name='お気に入りID',primary_key=True,max_length=20,validators=[RegexValidator(regex=r"^C[0-9]*$")])
   
    t5_user_id=models.ForeignKey(T5_user,verbose_name='店舗ID',on_delete=models.CASCADE,null=False)
    t12_charge_amount=models.PositiveIntegerField(verbose_name='チャージ額',blank=False,default=0)
    t12_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t12_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
    t12_charge_remain_ex=models.IntegerField(verbose_name='チャージ後残高',blank=False,default=0)
class T13_inquiry(models.Model):
     # t13_inquiry_id=models.CharField(verbose_name='お問い合わせID',primary_key=True,max_length=13,validators=[RegexValidator(regex=r"^I[0-9]*$")])
   
    t13_title=models.CharField(verbose_name='題名',max_length=30,blank=False)
    t13_sentence=models.TextField(verbose_name='内容',max_length=400,blank=False)
    t13_create_at=models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    t13_update_at=models.DateTimeField(verbose_name='最終更新日時',auto_now=True)
