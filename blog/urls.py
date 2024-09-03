from django.urls import path
from . import views  

# Importera views-modulen här

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
