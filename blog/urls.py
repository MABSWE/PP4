from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Welcome page
    path('blog/', views.BlogView.as_view(), name='blog'),  # Blog
    path('article/<int:pk>/', views.article_detail_view, name='article-detail'),  # Detail view with comments
    path('article/<int:pk>/comment/', views.add_comment, name='add_comment'),  # Add comment
    path('about/', views.about, name='about'),  # About Page
    path('login/', views.login_view, name='login'),  # Login Page
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout and redirect to home
    path('register/', views.register, name='register'),  # Register Page
    path("contact/", views.contact_view, name="contact"),  # Contact Page
    path("contact-success/", views.contact_success_view, name="contact-success"),  # Contact Success Page
]
