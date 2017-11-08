
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/',include('register.urls',namespace='register')),
    url(r'^loginpage/',include('loginpage.urls',namespace='loginpage')),
    url(r'^logoutpage/',include('logoutpage.urls',namespace='logoutpage')),
    url(r'^add_blog/',include('add_blog.urls',namespace='add_blog')),
    url(r'^delete_blog/',include('delete_blog.urls',namespace='delete_blog')),
    url(r'^update_blog/',include('update_blog.urls',namespace='update_blog')),
    url(r'^see_blog/',include('see_blog.urls',namespace='see_blog')),
    url(r'^recent/',include('recent.urls',namespace='recent')),
    url(r'^home/', include('templates.delete_blog.home.urls', namespace='home')),
    url(r'^popular/',include('popular.urls',namespace='popluar')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^comments/', include('django_comments.urls'))

]
