from django.shortcuts import render
from .forms import Registeration_form
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        if request.method=="GET":

            form = Registeration_form()
            template = loader.get_template('register/index.html')
            context={
                    "form":form
                }

            return HttpResponse(template.render(context,request))

        else:

            form = Registeration_form(request.POST)
            if form.is_valid():

                username=form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password=form.cleaned_data["password"]
                user=User()
                user.username=username
                user.email=email
                user.set_password(password)
                user.save()

                return HttpResponse("You have been registered")

            else:
                return HttpResponse("Invalid response")
    else:
        return HttpResponse("pehle log out krlo fir register krdena")