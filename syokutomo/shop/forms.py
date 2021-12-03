from django import forms
from .models import *
from prime.models import *

def wrap_boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)

class shop_updateForm(forms.ModelForm):
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


# class Food_createform(forms.ModelForm):
#     class Meta:
#         model=T4_food
#         fields=('t1_shop_id',"t9_food_category_id","t4_ingredients","t4_food_photo_01","t4_price","t4_food_name","t4_food_discribe",)