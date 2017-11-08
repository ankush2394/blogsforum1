from django.shortcuts import render
from add_blog .models import Blog
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from add_blog.models import rated_users_check
def index(request):

    blogs = Blog.objects.all().order_by('date').reverse()
    template= loader.get_template('recent/index.html')

    context={

        "blogs":blogs
    }

    return HttpResponse(template.render(context,request))

def index2(request,blog_id):

    if request.method=="GET":
        s = str(request.user.id) + str(blog_id)

        if rated_users_check.objects.filter(rated_user=s).exists() == False:

            template = loader.get_template('recent/index2.html')

            blog = Blog.objects.get(pk=blog_id)
            context={

                "blog":blog,
                "c_user":request.user
            }

            return HttpResponse(template.render(context,request))
        else:
            template = loader.get_template('recent/index3.html')

            blog = Blog.objects.get(pk=blog_id)
            context = {

                "blog": blog,
                "c_user": request.user
            }

            return HttpResponse(template.render(context, request))


    else :







        if not request.user.is_authenticated():

            return HttpResponse("You cant rate without logging in " )

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

            else :
                return HttpResponse("You have already rated this blog")


