from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate,login,logout
from .forms import Loginform
from captcha.fields import CaptchaField
# Create your views here.

def index(request):

    if request.method=="POST":

            username = request.POST['username']
            password = request.POST['password']

            user=authenticate(username=username,password=password)

            if user is not None:

                login(request, user)
                template = loader.get_template('loginpage/index3.html')
                c_user = request.user
                context={
                    "user":c_user
                }
                return HttpResponse(template.render(context,request))
            else:
                return HttpResponse("Enter correct details")

    else:

        if not request.user.is_authenticated:

            template = loader.get_template('loginpage/index.html')


            captcha=CaptchaField

            context={
                "captcha":captcha

            }

            return HttpResponse(template.render(context,request))

        else:

            template=loader.get_template('loginpage/index3.html')
            c_user=request.user
            context={
                "user":c_user
            }

            return HttpResponse(template.render(context,request))