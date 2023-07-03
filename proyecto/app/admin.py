from django.contrib import admin
from .models import AboutMe, Message, Profile, BlogPost

# Register your models here.

admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Message)
admin.site.register(AboutMe)