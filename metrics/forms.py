from django import forms
from .models import FacebookAccount

class FacebookAccountForm(forms.ModelForm):
    class Meta:
        model = FacebookAccount
        fields = ['account_id', 'account_name', 'access_token']