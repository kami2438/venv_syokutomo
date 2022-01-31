from dataclasses import field
from django import forms

from .models import *


class User_UpdateForm(forms.ModelForm):
    class Meta:
        model = T5_user
        fields = ("t5_user_firstname", "t5_user_lastname", "t5_address", "t5_post", "t5_tel_number", "t5_landmark", "t5_allergy", "t5_charge_tool",
                  "t5_credit_number", "t5_credit_limit", "t5_bank_name", "t5_bank_location", "t5_bank_number", "t5_bank_password")
        labels = {"t5_user_firstname":"苗字", "t5_user_lastname":"名前", "t5_address":"住所", "t5_post":"郵便番号", "t5_tel_number":"電話番号",
                  "t5_landmark":"自宅の目印", "t5_allergy":"控えるべき食材", "t5_charge_tool":"チャージ方法","t5_credit_number":"カード番号",
                   "t5_credit_limit":"有効期限", "t5_bank_name":"金融機関名", "t5_bank_location":"支店番号", "t5_bank_number":"口座番号", "t5_bank_password":"口座暗証番号"}











class Charge_form(forms.ModelForm):
    class Meta:
        model = T12_charge
        fields = '__all__'
        exclude = ['user','t12_create_at']

class Orderform(forms.ModelForm):
    class Meta:
        model =T2_order
        fields='__all__'
        exclude=['user','t2_create_at','t1_shop_id','t2_done']

class LikeForm(forms.Form):
   class Meta:
       model = T11_love
       fields = ('t1_shop_id', 'user')

class OrderDetailForm(forms.ModelForm):

    class Meta:
        model=T3_order_detail
        TIME_CHOICES = (('00:00:00', '00:00'),('00:30:00', '00:30'),

  ('01:00:00', '01:00'),('01:30:00', '01:30'),

  ('02:00:00', '02:00'),('02:30:00', '02:30'),

  ('03:00:00', '03:00'),('03:30:00', '03:30'),

  ('04:00:00', '04:00'),('04:30:00', '04:30'),

  ('05:00:00', '05:00'),('05:30:00', '05:30'),

  ('06:00:00', '06:00'),('06:30:00', '06:30'),

  ('07:00:00', '07:00'),('07:30:00', '07:30'),

  ('08:00:00', '08:00'),('08:30:00', '08:30'),

  ('09:00:00', '09:00'),('09:30:00', '09:30'),

  ('10:00:00', '10:00'),('10:30:00', '10:30'),

  ('11:00:00', '11:00'),('11:30:00', '11:30'),

  ('12:00:00', '12:30'),('12:30:00', '12:30'),
        ('13:00:00', '13:00'),('13:30:00', '13:30'),
        ('14:00:00', '14:00'),('14:30:00', '14:30'),
        ('15:00:00', '15:00'),('15:30:00', '15:30'),
        ('16:00:00', '16:00'),('16:30:00', '16:30'),
        ('17:00:00', '17:00'),('17:30:00', '17:30'),
        ('18:00:00', '18:00'),('18:30:00', '18:30'),
        ('19:00:00', '19:00'),('19:30:00', '19:30'),
        ('20:00:00', '20:00'),('20:30:00', '20:30'),
        ('21:00:00', '21:00'),('21:30:00', '21:30'),
        ('22:00:00', '22:00'),('22:30:00', '22:30'),
        ('23:00:00', '23:00'),('23:30:00', '23:30') )
        fields = '__all__'
        exclude=['user','t2_order_id','t1_shop_id','t3_review_done',"t3_order_deliver_status","t7_delivery_man_id","t3_create_at"
        "t3_update_at","t3_payment"]
        widgets={"t3_delivery_date":forms.Select(choices=TIME_CHOICES),
        # "t1_start_time":,"t1_end_time":
        }
    def __init__( self, *args):
        super(OrderDetailForm,self).__init__(*args, **kwargs)
        # id = kwargs.get("instance").user.id
        ord=T2_order.objects.filter(id=self.kwargs['pk'])
        self.fields['t4_food_id'].queryset = T4_food.objects.filter(t1_shop_id=ord.t1_shop_id)