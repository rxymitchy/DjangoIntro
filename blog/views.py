from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #class based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from .models import Post
from django.contrib.auth.models import User
#from django.http import HttpResponse

#dummy data which is a list of dictionaries
#what the user will see(view)
def home(request):
    #creating a dictionary to hold the posts
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) 
    #title ere left as default
    #makes context data accessible to templates


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    #put instead of creating context if its short
    #return HttpResponse('<h1>Blog About</h1>')

#displays all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #arranges from new to old posts
    paginate_by = 2 #2 posts per page
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
#displays  specific post of a specific individual
class PostDetailView(DetailView):
    model = Post

#creates posts for specific user
#ensures only logged in users can create posts - LoginRequiredMixin
class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#ensures users can only edit their own posts - UserPassesTestMixin
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() #gets postcurrently being updated
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #returns to home after deletion

    def test_func(self):
        post = self.get_object() #gets postcurrently being updated
        if self.request.user == post.author:
            return True
        return False
