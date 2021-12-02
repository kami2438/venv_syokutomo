from django import forms
from .models import *

class driver_updateForm(forms.ModelForm):
    class Meta:
        model = T7_delivery_man
        fields = '__all__'
        exclude = ['user','t1_create_at']
        labels = {"t7_delivery_man_firstname":"苗字","t7_delivery_man_lastname":"名前","t7_delivery_man_tel":"電話番号","t7_bank_name":"金融機関名","t7_bank_location":"支店番号","t7_bank_number":"口座番号"}