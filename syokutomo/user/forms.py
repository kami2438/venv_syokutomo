from django import forms
from .models import *


class User_UpdateForm(forms.ModelForm):
    class Meta:
        model = T5_user
        fields = ("t5_user_firstname", "t5_user_lastname", "t5_address", "t5_post", "t5_tel_number", "t5_landmark", "t5_allergy", "t5_charge_tool",
                  "t5_credit_number", "t5_credit_limit", "t5_bank_name", "t5_bank_location", "t5_bank_number", "t5_bank_password")
