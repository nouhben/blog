from django.urls import path
from . import views
#to test the class based views
from .views import PostListView, PostDetailView, PostCreatView, PostUpdateView, PostDeleteView, UserPostListView
urlpatterns = [
    path('',views.home, name="blog-home"),
    #path('', PostListView.as_view(), name='blog-home'),
    
    #route that takes us to specefic post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path to update a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #to create and update a post
    path('post/new/', PostCreatView.as_view(), name='post-create'), #it is excpecting template called: post_form.html
    #path to delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # Posts for a pretecular user
     path('user/<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
    path('business/',views.business, name="blog-business"),
    path('tech/',views.tech, name="blog-tech"),
    path('health/',views.health, name="blog-health"),
    path('edu/',views.edu, name="blog-edu"),
    path('visa/',views.health, name="blog-visa"),
    path('help/',views.edu, name="blog-help"),
    path('islam/',views.edu, name="blog-islam"),
    path('design/',views.edu, name="blog-design"),
    path('style/',views.edu, name="blog-style"),
]
