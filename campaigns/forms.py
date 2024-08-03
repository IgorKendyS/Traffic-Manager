from django import forms

class CampaignForm(forms.Form):
    file = forms.FileField()
