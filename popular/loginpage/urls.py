from django.conf.urls import url,include
from django.contrib import admin
from . import views

app = 'loginpage'


urlpatterns = [
    url(r'^$', views.index,name='index'),
    ]