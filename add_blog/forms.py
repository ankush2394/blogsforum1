from django.forms import ModelForm
from .models import Blog
from django import forms
class blogform(ModelForm):

    content = forms.CharField(widget=forms.Textarea)

    class Meta:

        model = Blog

        fields=[

            "title",
            "sub_title",
            "content",
            "rating"

        ]