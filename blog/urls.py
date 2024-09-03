from django.urls import path
from . import views  # Importera views-modulen här

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Exempel på en URL
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    # Lägg till andra URL-mönster här
]
