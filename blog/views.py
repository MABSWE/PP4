from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Post
from .forms import ContactForm  

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Contact Page
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simulated
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "All fields are required. Please fill out the form.")
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

# Success Page for Contact Form
def contact_success_view(request):
    return render(request, "contact_success.html")
