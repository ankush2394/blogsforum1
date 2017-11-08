from django.conf.urls import url,include
from django.contrib import admin

from . import views

app='recent'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<blog_id>[0-9]+)/$',views.index2,name='index2')

]
