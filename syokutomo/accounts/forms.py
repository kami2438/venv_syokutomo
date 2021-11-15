# forms.py
from allauth.account.forms import SignupForm
from django import forms
from .import models


class CustomSignupForm(SignupForm):  # SignupFormを継承する
    forms.fields.ChoiceField(
        choices=CustomUser.type_choice.choices,
        required=True,
        label='タイプ',
        # widget=forms.widgets.Select,
    )
    user_type = form

    def signup(self, request, user):
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
