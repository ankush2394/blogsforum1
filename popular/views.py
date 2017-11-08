from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from add_blog.models import Blog
from add_blog.models import rated_users_check
from add_blog.models import Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from datetime import datetime


def index(request):

    blogs = Blog.objects.all().order_by('rating').reverse()
    template= loader.get_template('popular/index.html')
    context={
        "blogs":blogs
    }
    return HttpResponse(template.render(context,request))


def index2(request,blog_id):

    if request.method=="GET":
        s = str(request.user.id) + str(blog_id)
        if rated_users_check.objects.filter(rated_user=s).exists() == False:
            form = CommentForm()
            blog = Blog.objects.get(pk=blog_id)
            comments = Comment.objects.filter(blog=blog)

            template = loader.get_template('popular/index2.html')


            context={

                "blog":blog,
                "c_user": request.user,
                "form":form,
                "comments":comments

            }

            return HttpResponse(template.render(context,request))
        else:
            template = loader.get_template('popular/index3.html')
            form = CommentForm()
            blog = Blog.objects.get(pk=blog_id)
            comments = Comment.objects.filter(blog=blog)

            context = {

                "blog": blog,
                "c_user": request.user,
                "form": form,
                "comments": comments

            }

            return HttpResponse(template.render(context, request))

    else :







        if not request.user.is_authenticated():

            return HttpResponse("You cant rate and comment without logging in " )

        else:
            # first check for redundancy and then allow to store it in the database

            s = str(request.user.id)+str(blog_id)

            if rated_users_check.objects.filter(rated_user=s).exists()==False:

                num = request.POST['rating']
                curr_blog = Blog.objects.get(pk=blog_id)
                curr_blog.rating *= curr_blog.count
                curr_blog.rating += float(num)
                curr_blog.count += 1
                curr_blog.rating = curr_blog.rating/curr_blog.count
                curr_blog.save()
                rated_users_check(rated_user=s).save()

                return HttpResponse("Thanks for the fucking rating")






            form = CommentForm(request.POST)

            if form.is_valid():
                text=form.cleaned_data['text']
                author = request.user
                date = datetime.now()
                blog = Blog.objects.get(pk=blog_id)

                comment = Comment(blog=blog,author=author,text = text,created_date=date)
                comment.save()
                return HttpResponseRedirect('/popular/'+str(blog_id))
            else:
                return HttpResponse("invalid")