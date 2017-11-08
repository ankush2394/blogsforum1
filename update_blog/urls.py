from django.conf.urls import url,include
from django.contrib import admin
from . import views

app = 'update_blog'


urlpatterns = [
    url(r'^$', views.index1,name='index1'),
    url(r'^(?P<blog_id>[0-9]+)/$',views.index2,name='index2')
    ]