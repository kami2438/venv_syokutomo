from dataclasses import field
from django import forms

from syokutomo.prime.models import T2_order
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
        exclude=['user','t2_create_at','t1_shop_id']