from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost, Message

class SearchPosts(forms.Form):
    search = forms.CharField(required=False)

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repete password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { key: '' for key in fields }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'summary', 'category', 'content', 'image']
        widgets = {
            'content': CKEditorWidget()
        }

class ProfileForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    name = forms.CharField()
    lastname = forms.CharField()
    profile_image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)
    webpage = forms.CharField()

class SelectRecipientForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label='To')
    
class MessageForm(forms.Form):
    message_input = forms.CharField(label='', widget=forms.Textarea)


