"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name="Home"),
    path('register', views.registeruser, name="Register"),
    path('login', views.login, name="Login"),
    path('logout', views.Logout.as_view(), name='Logout'),
    path('about-me', views.about, name="About"),
    path('blog-posts', views.postslist, name="Blog_Posts"),
    path('my-posts', views.myposts, name="My_Posts"),
    path('edit-post', views.managepost, name="Create_Post"),
    path('edit-post/<int:post_id>/', views.managepost, name="Edit_Post"),
    path('blog-post/<int:post_id>/', views.detailpost, name="Detail_Post"),
    path('delete-post/<int:post_id>/', views.deleteblog, name='Delete_Blog'),
    path('edit-profile', views.manageprofile, name="Edit_Profile"),
    path('profile/<username>', views.myprofile, name="Profile"),
    path('messages', views.messages, name="Messages"),
    path('conversation/<username>', views.conversation, name="Conversation"),
]
