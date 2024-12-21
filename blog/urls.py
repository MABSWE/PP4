from django.urls import path
from . import views  

# Importera views-modulen här

urlpatterns = [
    path('', views.home, name='home'),  # Welcome page
    path('blog/', views.BlogView.as_view(), name='blog'),  # Blog
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
]
