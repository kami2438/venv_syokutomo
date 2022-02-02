from django import forms
from django.core.mail import EmailMessage
from .models import *
from django.utils import timezone

class ReservationForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(
            name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message,
                               from_email=from_email, to=to_list, cc=cc_list)
        message.send()

def wrap_boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)
class Regis_userForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['t5_allergy'].delimiter = '、'
        self.label_suffix = " "
    class Meta:
        model = T5_user
        fields = ("t5_user_firstname", "t5_user_lastname","t5_tel_number", "t5_landmark", "t5_allergy", "t5_charge_tool",
                   "t5_credit_number", "t5_credit_limit", "t5_credit_security", "t5_bank_name", "t5_bank_location", "t5_bank_number", "t5_bank_password")
        help_texts={
            't5_allergy':"例）たまご、かに、なす　のように区切りに読点を使ってください"
        }
        widgets={
            # "t5_credit_security":forms.PasswordInput(),"t5_bank_password":forms.PasswordInput()
            }
        
        # def __init__(self,*args,**kwargs) :
        #     super().__init__(self,*args,**kwargs)
        #     for field in self.fields.values():
        #         field.widget.attrs['class'] = 'form-control col-9'
        #         field.widget.attrs['placeholder'] = "{v_placeholder}を入力してください".format(v_placeholder=field.verbose_name)


class Regis_shopForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    # t1_start_time = forms.ChoiceField(choices=TIME_CHOICES,queryset=T1_shop.objects)
    # t1_end_time = forms.ChoiceField(choices=TIME_CHOICES,queryset=T1_shop.objects)
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
        exclude = ['user','t1_create_at',"t1_favorite_count","t1_review_ave"]
        widgets={"t1_shop_sun":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_mon":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tue":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_wed":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_tru":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_shop_fri":forms.CheckboxInput(check_test=wrap_boolean_check),
        "t1_shop_sat":forms.CheckboxInput(check_test=wrap_boolean_check),"t1_start_time":forms.Select(choices=TIME_CHOICES),"t1_end_time":forms.Select(choices=TIME_CHOICES),
        # "t1_start_time":,"t1_end_time":
        }


class Regis_driverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    class Meta:
        model = T7_delivery_man
        fields = '__all__'
        exclude = ['user','t1_create_at']