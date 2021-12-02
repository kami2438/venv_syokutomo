from django import forms
from .models import *

class shop_infoForm(forms.ModelForm):
    class Meta:
        model = T1_shop
        fields = '__all__'
        exclude = ['user','t1_create_at',"t1_favorite_count","t1_review_ave"]
        widgets={"t1_shop_sun":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_mon":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tue":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_wed":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tru":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_fri":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_sat":forms.CheckboxInput(check_test=wrap_boolean_check)
        # "t1_start_time":,"t1_end_time":
        }