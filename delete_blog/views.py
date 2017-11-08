from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
def index1(request):

    template = loader.get_template('delete_blog/index.html')
    c_user=request.user
    context={

        "user":c_user
    }

    return HttpResponse(template.render(context,request))

def index2(request,blog_id):

    c_user=request.user
    blog=c_user.blog_set.get(pk=blog_id)
    blog.delete()
    return HttpResponseRedirect("/delete_blog/")