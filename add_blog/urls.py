from django.conf.urls import url,include
from django.contrib import admin
from . import views

app = 'add_blog'


urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    ]