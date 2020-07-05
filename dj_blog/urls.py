from django.contrib import admin
from django.urls import path, include
#import the users views
from users import views as user_views
from django.contrib.auth import views as auth_views
#to serve files durind dev
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('blog.urls')),
    #path('blog/',include('blog.urls')),
        #add the users management pathes later we can add the to users urls.py
    path('register/', user_views.register, name='user-register'),
        #login and logout vies
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('login/', user_views.MyLoginView.as_view(template_name='users/login.html'), name='login'),
    #path('login/', user_views.MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #profiles
    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
