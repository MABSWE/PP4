from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'