from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate

def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('loginpage/index3.html')
        context = {
        }
        return HttpResponse(template.render(context, request))



    else:

        template= loader.get_template('home/index.html')
        context={
        }
        return HttpResponse(template.render(context,request))