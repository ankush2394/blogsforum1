from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class Loginform(ModelForm):
    captcha = CaptchaField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User

        fields = [

            "username",
            "password",
            "captcha"
        ]