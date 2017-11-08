from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User

class Registeration_form(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:

        model=User

        fields=[
            "username",
            "email",
            "password"
        ]
