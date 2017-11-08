from django.shortcuts import render
from .forms import blogform
from django.template import loader
from django.http import HttpResponse
from .models import Blog
from datetime import datetime
def index1(request):
    if request.user.is_authenticated:

        if(request.method=="GET"):

            template = loader.get_template('add_blog/index.html')
            form = blogform()
            c_user=request.user
            context={

                "user":c_user,
                "form":form
            }

            return HttpResponse(template.render(context,request))
        else:

            form=blogform(request.POST)

            if form.is_valid():
                c_user = request.user
                title=form.cleaned_data['title']
                sub_title=form.cleaned_data['sub_title']
                content = form.cleaned_data['content']
                rating = form.cleaned_data['rating']
                date = datetime.now()
                blog = Blog(user=c_user,title=title,sub_title=sub_title,content=content,rating=rating,date=date)
                blog.save()
                return HttpResponse("Your blog is saved .")

            else:
                return HttpResponse("invalid form")
    else:
        return HttpResponse("Pehle login to krlo :p")