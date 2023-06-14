from django.template import Context
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from .utils import get_article_by_id
from .models import BlogPost, AppUser, Profile
from .forms import PostsForm, SearchPosts, AppUserForm, ProfileForm

def inicio(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about-me.html")

def postslist(request):
    if request.method == 'POST':
        my_form = SearchPosts(request.POST)
        if my_form.is_valid():
            info = my_form.cleaned_data
            blogs = BlogPost.objects.filter(title__icontains=info["search"])
            return render(request, "app/blog-posts.html", {'blogs': blogs, 'my_form': SearchPosts()})
    else:
        blogs = BlogPost.objects.all()
        return render(request, "app/blog-posts.html", {'blogs': blogs, 'my_form': SearchPosts()})
    
def manageposts(request):
    print('request.method ',request.method)
    if request.method == 'POST':
        my_form = PostsForm(request.POST)
        print('is_valid', my_form.errors)
        if my_form.is_valid():
            info = my_form.cleaned_data
            user_id = my_form.cleaned_data['app_user'].id
            blog = BlogPost(app_user_id=user_id,title=info['title'],summary=info['summary'],content=info['content'],category=info['category'],image=info['image'])
            blog.save()

    my_form = PostsForm()
    blogs = BlogPost.objects.all()
    return render(request, "app/manage-posts.html", {'my_form': my_form, 'blogs': blogs})

def manageusers(request):
    if request.method == 'POST':
        my_form =AppUserForm(data=request.POST)

        if my_form.is_valid():
            info = my_form.cleaned_data
            exists = AppUser.objects.filter(username=info['username']).exists()

            if not exists:
                user = AppUser(username=info['username'],password=info['password'],email=info['email'])
                user.save()

    my_form = AppUserForm()
    users = AppUser.objects.all()
    return render(request, "app/manage-users.html", {'my_form': my_form, 'users': users})

def manageprofiles(request):
    if request.method == 'POST':
        my_form =ProfileForm(request.POST, request.FILES)
        if my_form.is_valid():
            info = my_form.cleaned_data
            user_id = my_form.cleaned_data['app_user'].id
            profile = Profile(app_user_id=user_id,name=info['name'],lastname=info['lastname'],profile_image=info['profile_image'],description=info['description'],webpage=info['webpage'])
            profile.save()

    my_form = ProfileForm()
    profiles = Profile.objects.all()
    print(profiles)
    return render(request, "app/manage-profiles.html", {'my_form': my_form, 'profiles': profiles})

# def post(request, id):
#     article = get_article_by_id(id)
#     return render(request, "app/post.html", article)

