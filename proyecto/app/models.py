from django.db import models
from ckeditor.fields import RichTextField
    
class AppUser(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.username

class Profile(models.Model):
    app_user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    profile_image = models.ImageField(upload_to='static/app/blog_images/', null=True)
    description = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.lastname}"

class BlogPost(models.Model):
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    category = models.CharField(max_length=40)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/app/blog_images/', null=True)

    def __str__(self):
        return self.title

