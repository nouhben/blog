from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
# Create your views here.
#import my models
from .models import Post
@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'home',
        'side_bar':False,
    }
    return render(request, 'blog/index.html', context)
@login_required
def business(request):
    return render(request,'blog/business.html')
@login_required
def tech(request):
    return render(request, 'blog/tech.html',{})
@login_required
def health(request):
    return render(request,'blog/health.html')
@login_required
def edu(request):
    return render(request,'blog/edu.html')

# Class based views
from django.views.generic import ListView
class PostListView(ListView):
    #for pagination
    paginate_by = 5
    # we need to create the model variable
    model = Post
    # we need to specify template name by deafault it is
    # app/modelName_viewType.html exp: blog/post_list.html
    # since we have our home we can modify this behaviour here:
    #template_name = 'blog/index.html'
    # but the template has the posts we passed in the context
    # and the CBV does not have that context dictionnary
    # the default variable that is equivalent to posts is called
    # objectsList => so we can either eterate over it in the template 
    # and change posts into objectList or we can do 
    # this here on teh view:
    context_object_name = 'posts'
    # to reverse the order of our posts from oldest-new to newst-olds
    # ordering = ['date_posted'] 

from django.shortcuts import get_object_or_404 
from django.contrib.auth.models import User
class UserPostListView(ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        posts = Post.objects.filter(author=user)
        return posts#.order_by('date_posted')


# For each post individualy it is a detail view
from django.views.generic import DetailView
class PostDetailView(DetailView):
    model = Post
    # with this view we used everything by default 
    # temlate name and object as post

#CRUD class based views
from django.views.generic import CreateView, UpdateView, DeleteView
class PostCreatView(CreateView):
    model = Post
    fields = ['title','description','content'] #fields we want to be in the form
    # validate the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/'
    #success_url = '/blog/'

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # for only the author of the post who can update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

from django.views.generic import DeleteView
class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
    success_url = '/'
