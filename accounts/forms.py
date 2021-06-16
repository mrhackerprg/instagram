from django import forms
from django.forms import fields
from .models import Info

class Informations(forms.ModelForm):
    class Meta:
        model = Info
        fields = ["username" , "password"]
