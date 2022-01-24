from django import forms
from .models import *
from prime.models import *

def wrap_boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)

class shop_updateForm(forms.ModelForm):
    class Meta:
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
        model = T1_shop
        fields = '__all__'
        exclude = ['user','t1_create_at',"t1_favorite_count","t1_review_ave","t1_shop_photo_03","t1_shop_photo_04","t1_shop_photo_05"]
        widgets={"t1_shop_sun":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_mon":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tue":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_wed":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tru":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_fri":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_sat":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_start_time":forms.Select(choices=TIME_CHOICES),"t1_end_time":forms.Select(choices=TIME_CHOICES),
        # "t1_start_time":,"t1_end_time":
        }


class Food_createform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['t4_ingredients'].delimiter = '、'
    class Meta:
        model=T4_food
        fields=("t9_food_category_id","t4_ingredients","t4_food_photo_01","t4_price","t4_food_name","t4_food_discribe",)
        exclude=['t1_shop_id']
        help_texts={
            't4_ingredients':"例）たまご、かに、なす　のように区切りに読点を使ってください"
        }