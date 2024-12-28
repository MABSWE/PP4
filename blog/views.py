from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Post, Comment
from .forms import ContactForm, CommentForm, PostForm

# Home View (Welcome)
def home(request):
    return render(request, 'home.html')

# Blog Page with Post Creation
def blog_view(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been added!")
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog.html', {'posts': posts, 'form': form})

# Detail view with Comments
def article_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added!")
            return redirect('article-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'detail_view.html', {'post': post, 'form': form, 'comments': comments})

# Add Comment View
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added!")
    return redirect('article-detail', pk=post.pk)

# About Page
def about(request):
    return render(request, 'about.html')

# Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {username}!")
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# Register Page
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created for {user.username}! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Contact Page
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Success Page for Contact Form
def contact_success_view(request):
    return render(request, "contact_success.html")
