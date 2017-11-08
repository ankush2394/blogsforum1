from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.template import loader
from django.http import HttpResponse
from add_blog.models import Blog
from django.http import HttpResponseRedirect
def index1(request):

    template = loader.get_template('see_blog/index.html')
    c_user=request.user
    blogs=Blog.objects.filter(user=c_user)
    context={

        "user":c_user,
        "blogs":blogs
    }

    return HttpResponse(template.render(context,request))

def index2(request,blog_id):

    template = loader.get_template('see_blog/index2.html')
    c_user=request.user
    blog = c_user.blog_set.get(pk=blog_id)
    context={
        "user":c_user,
        "blog":blog
    }

    return HttpResponse(template.render(context,request))