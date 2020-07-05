from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterFrom, ContactForm, ColorfulContactForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.views import LoginView
#to use with a FBV decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_creation_form = UserRegisterFrom(request.POST)
        if user_creation_form.is_valid():
            #save the form to the DB
            user_creation_form.save()
            username = user_creation_form.cleaned_data.get('username')
            #messages.success(request,f'Account created for {username}!')
            messages.success(request,f'Account created {username} Please Login!')
            #return redirect('blog-home')
            return redirect('login')
    else:
        user_creation_form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form':user_creation_form})
     
#the login required decorator will only allow users that are authenticated to go that route i.e view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, 
            request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/profile.html',context)
#to login and display success message to the user it is better to go like this
# from django.contrib.messages.views import SuccessMessageMixin
# class MyLoginView(SuccessMessageMixin ,LoginView):
#     template_name = 'users/login.html'
#     success_url = 'blog-home'
#     success_message = 'Welcome to your profile'
def testingForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()

    return render(request, 'users/testing.html', {'form':form, 'color':ColorfulContactForm()})