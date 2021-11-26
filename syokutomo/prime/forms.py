from django import forms
from django.core.mail import EmailMessage
from .models import *


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


class Regis_userForm(forms.ModelForm):
    class Meta:
        model = T5_user
        fields = ("t5_user_firstname", "t5_user_lastname", "t5_address","t5_post", "t5_tel_number", "t5_landmark", "t5_allergy", "t5_charge_tool",
                   "t5_credit_number", "t5_credit_limit", "t5_credit_security", "t5_bank_name", "t5_bank_location", "t5_bank_number", "t5_bank_password")
        # def __init__(self,*args,**kwargs) :
        #     super().__init__(self,*args,**kwargs)
        #     for field in self.fields.values():
        #         field.widget.attrs['class'] = 'form-control col-9'
        #         field.widget.attrs['placeholder'] = "{v_placeholder}を入力してください".format(v_placeholder=field.verbose_name)


class Regis_shopForm(forms.ModelForm):
    class Meta:
        model = T1_shop
        fields = '__all__'
        exclude = ['user'],['t1_create_at']

class Regis_deliveryForm(forms.ModelForm):
    class Meta:
        model = T7_delivery_man
        fields = '__all__'
        exclude = ['user'],['t1_create_at']