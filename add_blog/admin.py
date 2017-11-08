from django.contrib import admin
from . models import Blog
from .models import rated_users_check
from .models import Comment
# Register your models here.
admin.site.register(Blog)
admin.site.register(rated_users_check)
admin.site.register(Comment)
