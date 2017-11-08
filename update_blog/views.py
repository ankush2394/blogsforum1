from .forms import Update_form
from django.template import loader
from django.http import HttpResponse
from add_blog.models import Blog
def index1(request):

    template = loader.get_template('update_blog/index.html')
    c_user=request.user
    context={

        "user":c_user
    }

    return HttpResponse(template.render(context,request))

def index2(request,blog_id):

    if request.method == "GET":
        c_user=request.user
        #form ko automatic bharna ho to yeh krlo:p

        form = Update_form(instance=c_user.blog_set.get(id=blog_id))
        template = loader.get_template('update_blog/index2.html')
        c_user = request.user
        context={
                "blog_id":blog_id,
                "user":c_user,
                "form":form
            }


        return HttpResponse(template.render(context,request))

    else:

        form = Update_form(request.POST)

        if form.is_valid():
            c_user = request.user
            blog = c_user.blog_set.get(pk=blog_id)
            title = form.cleaned_data['title']
            sub_title = form.cleaned_data['sub_title']
            content = form.cleaned_data['content']
            rating = form.cleaned_data['rating']

            blog.title=title
            blog.sub_title=sub_title
            blog.content=content
            blog.rating = rating
            #blog = Blog(user=c_user, title=title, sub_title=sub_title, content=content)
            blog.save()
            return HttpResponse("Your blog is updated .")

        else:
            return HttpResponse("invalid form")
