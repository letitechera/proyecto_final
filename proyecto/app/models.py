from django.db import models
from ckeditor.fields import RichTextField

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.username

class Profile(User):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    profile_image = models.ImageField(upload_to='profile_images')
    description = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.lastname}"

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image_link = models.URLField()
    image_posted_date = models.DateField()

    def __str__(self):
        return self.title

# Create your models here.
