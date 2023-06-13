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
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about-me', views.about, name="About me"),
    path('blog-posts', views.postslist, name="Blog_Posts"),
    path('manage-posts', views.manageposts, name="Manage_Posts"),
    path('manage-users', views.manageusers, name="Manage_Users"),
    path('manage-profiles', views.manageprofiles, name="Manage_Profiles"),
    # path('post/<int:id>', views.post, name="Blog_Post_Detail"),
    # path('edit-post/<id>', views.post, name="Edit_Post"),
    # path('delete-post/<id>', views.deletepost, name="Delete_Post"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)