from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    prepopulated_fields = {'slug': ('title',)} 

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)