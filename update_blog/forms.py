from django.forms.models import ModelForm
from add_blog.models import Blog
from django import forms

class Update_form(ModelForm):


    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog

        fields = [

            "title",
            "sub_title",
            "content",
            "rating"

        ]