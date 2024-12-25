from django.urls import path
from . import views  

# Importera views-modulen här

urlpatterns = [
    path('', views.home, name='home'),  # Welcome page
    path('blog/', views.BlogView.as_view(), name='blog'),  # Blog
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('about/', views.about, name='about'),  # About Page
    path('login/', views.login_view, name='login'),  # Login Page
    path('register/', views.register, name='register'),  # Register Page
    path("contact/", views.contact_view, name="contact"),  # Contact Page
    path("contact-success/", views.contact_success_view, name="contact-success"),  # Contact Success Page
]