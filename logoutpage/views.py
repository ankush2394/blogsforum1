from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def index(request):
    logout(request)
    messages.add_message(request,messages.INFO, "You have been logged out safely.")
    return HttpResponseRedirect("/loginpage/")