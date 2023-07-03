from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Max 
from .models import AboutMe, BlogPost, Message, Profile
from .forms import AboutMeForm, BlogPostForm, MessageForm, SearchPosts, ProfileForm, RegisterUserForm, SelectRecipientForm
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
import os

def inicio(request):
    latest_posts = BlogPost.objects.order_by('-date')[:3]
    return render(request, "app/index.html", {'latest_posts': latest_posts})

def about(request):
    about_me_info = AboutMe.objects.first()

    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=about_me_info)
        if form.is_valid():
            form.save()
            return redirect('About')  # Redirect to the updated "About Me" page
    
    else:
        form = AboutMeForm(instance=about_me_info)
    
    return render(request, 'app/about-me.html', {'form': form, 'about_me':about_me_info})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                django_login(request, user)
                return redirect("Home")
            else:
                return render(request, "app/login.html", {"message":"Username or password are incorrect"})

    form = AuthenticationForm()
    return render(request, "app/login.html", {"form": form})

def postslist(request):
    if request.method == 'POST':
        my_form = SearchPosts(request.POST)
        if my_form.is_valid():
            info = my_form.cleaned_data
            blogs = BlogPost.objects.filter(title__icontains=info["search"]).order_by('-date')
            return render(request, "app/blog-posts.html", {'blogs': blogs, 'my_form': SearchPosts()})
    else:
        blogs = BlogPost.objects.order_by('-date')
        return render(request, "app/blog-posts.html", {'blogs': blogs, 'my_form': SearchPosts()})   
    
    
def registeruser(request):
    if request.method == 'POST':
        my_form =RegisterUserForm(data=request.POST)

        if my_form.is_valid():
            info = my_form.cleaned_data
            exists = User.objects.filter(username=info['username']).exists()

            if not exists:
                my_form.save()
                return redirect("Login")
            else:
                return render(request, "app/register.html", {'my_form': RegisterUserForm()})
        else:
            return render(request, 'app/register.html', {'my_form': my_form})

    return render(request, "app/register.html", {'my_form': RegisterUserForm()})

@login_required
def manageprofile(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        my_form =ProfileForm(request.POST, request.FILES)
        if my_form.is_valid():
            info = my_form.cleaned_data
            if info.get('email'):
                user.email = info.get('email')
            if info.get('username'):
                user.username = info.get('username')
            if info.get('name'):
                profile.name = info.get('name')
            if info.get('lastname'):
                profile.lastname = info.get('lastname')
            if info.get('description'):
                profile.description = info.get('description')
            if info.get('webpage'):
                profile.webpage = info.get('webpage')

            profile.profile_image = info.get('profile_image') if info.get('profile_image') else profile.profile_image

            user.save()
            profile.save()
            
            return render(request, "app/profile.html", {'profile': profile})

        else:
            return render(request, "app/edit-profile.html", {'my_form': my_form})
            
    form = ProfileForm(
        initial={
            'username':user.username,
            'email':user.email,
            'name':profile.name,
            'lastname':profile.lastname,
            'description':profile.description,
            'webpage':profile.webpage,
            'profile_image':profile.profile_image
        }
    )
    return render(request, "app/edit-profile.html", {'my_form': form})

@login_required
def myprofile(request, username):
    userFound = User.objects.get(username=username)
    profile, _ = Profile.objects.get_or_create(user=userFound)
    return render(request, "app/profile.html", {'profile': profile})

@login_required
def myposts(request):
    blogs = BlogPost.objects.filter(user=request.user).order_by('-date')
    return render(request, "app/my-posts.html", {'blogs': blogs})

@login_required
def managepost(request, post_id=None):
    if post_id:
        blog_post = get_object_or_404(BlogPost, pk=post_id)
    else:
        blog_post = None

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            info = form.cleaned_data
            blog_post.image = info.get('image') or blog_post.image
            blog_post.save()

            blogs = BlogPost.objects.filter(user=request.user).order_by('-date')
            return render(request, "app/my-posts.html", {'blogs': blogs})
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, "app/edit-post.html", {'my_form': form})

def detailpost(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "app/post.html", {'blog': post})

@login_required
def deleteblog(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    blog_post.delete()
    blogs = BlogPost.objects.filter(user=request.user).order_by('-date')
    return render(request, "app/my-posts.html", {'blogs': blogs})

@login_required
def messages(request):
    if request.method == 'POST':
        form = SelectRecipientForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            to_user = info["recipient"]
            return redirect('Conversation', username=to_user)

    conversations = Message.objects.filter(
        Q(from_user=request.user) | Q(to_user=request.user)
    ).values('from_user', 'to_user').distinct()

    usersFound = User.objects.filter(
        Q(id__in=[c['from_user'] for c in conversations]) |
        Q(id__in=[c['to_user'] for c in conversations])
    ).exclude(id=request.user.id)

    contacts = Profile.objects.filter(user__id__in=usersFound).exclude(id=request.user.id)

    for contact in contacts:
        contact.last_message = Message.objects.filter(
            Q(from_user=request.user, to_user=contact.user) |
            Q(from_user=contact.user, to_user=request.user)
        ).order_by('-date').first()

    return render(request, 'app/messages.html', {'contacts': contacts, 'form': SelectRecipientForm()})

@login_required
def conversation(request, username):
    with_user = User.objects.get(username=username)
    with_user.profile, _ = Profile.objects.get_or_create(user=with_user)

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            if info.get('message_input'):
                new_message = Message()
                new_message.message = info.get('message_input')
                new_message.from_user = request.user
                new_message.to_user = with_user
                new_message.save()
                return redirect('Conversation', username=username)

    messages = Message.objects.filter(
        (Q(from_user=request.user) & Q(to_user=with_user)) |
        (Q(from_user=with_user) & Q(to_user=request.user))
    ).order_by('-date')

    return render(request, 'app/conversation.html', {'contact': with_user, 'messages': messages, 'form': form})

class Logout(LogoutView):
    template_name = 'app/index.html'