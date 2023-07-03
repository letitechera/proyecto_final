from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    profile_image = models.ImageField(upload_to='avatars/', null=True)
    description = models.CharField(max_length=1000)
    webpage = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username}"

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    category = models.CharField(max_length=40)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class AboutMe(models.Model):
    image = models.ImageField(upload_to='about_me_images')
    description = RichTextField(null=True)
    header = models.CharField(max_length=1000, null=True)
