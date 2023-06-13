from django import forms
from app.models import AppUser

class SearchPosts(forms.Form):
    search = forms.CharField(required=False)

class PostsForm(forms.Form):
    app_user = forms.ModelChoiceField(queryset=AppUser.objects.all())
    title = forms.CharField()
    summary = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.CharField()
    image = forms.ImageField(required=False)

class AppUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()

class ProfileForm(forms.Form):
    app_user = forms.ModelChoiceField(queryset=AppUser.objects.all())
    name = forms.CharField()
    lastname = forms.CharField()
    profile_image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)
    webpage = forms.CharField()
    
