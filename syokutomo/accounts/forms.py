# forms.py
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser


class CustomSignupForm(SignupForm):  # SignupFormを継承する
    # forms.fields.ChoiceField(
    #     choices=CustomUser.type_choice,
    #     required=True,
    #     label='タイプ'
    #     # widget=forms.widgets.Select,
    # )
    # last_name = forms.CharField(max_length=30, label='名字')
    # user_type = form
    user_type= forms.CharField(
        widget=forms.Select(choices=CustomUser.type_choice),label="利用者する種別",required=True)
    area= forms.ForeignKey(
        label="在住エリア",required=True
    )
    class Meta:
        model=CustomUser

    # def signup(self, request):
    #     user= super(CustomSignupForm, self).save(request)
    #     user.user_type = self.cleaned_data['user_type']
    #     # user.last_name = self.cleaned_data['last_name']
    #     user.save()
    #     # return user
