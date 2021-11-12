from django.db import models

# Create your models here.


class T1_shop(models.Model):
    t1_shop_id = models.CharField(verbose_name='店舗ID',null=true,primary_key= true,max_length=10)
    t1_shop_name_prime = models.CharField(verbos_name= '店名',max_length=3,null=False)
    t1_area_id= models.ForeignKey(verbose_name='エリアID', T10_area, on_delete=models.CASCADE)
    t1_address= models.CharField(verbos_name= '住所',max_length=200,null=False)
    t1_shop_category_id= models.ForeignKey(verbose_name='店舗カテゴリーID',max_length=4,on_delete=models.CASCADE)
    t1_holiday=models.IBinaryField(verbose_name='定休日',max_length=1)
    t1_start_time=models.DateTimeField(verbose_name='注文開始時間',auto_now_add=Ture)
    t1_end_time=models.DateTimeField(verbose_name='注文終了時間')
