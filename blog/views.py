from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Home View (Welcome)
def home(request):
    return render(request, 'home.html')

# Blog Page
class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

# Detail view
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'
    context_object_name = 'post'

# About Page
def about(request):
    return render(request, 'about.html')

# Login Page
def login_view(request):
    return render(request, 'login.html')

# Register Page
def register(request):
    return render(request, 'register.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')
