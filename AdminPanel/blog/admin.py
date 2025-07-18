

# Register your models here.
from django.contrib import admin
from .models import BlogPost

# Customize how BlogPost appears in admin
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Columns shown
    search_fields = ('title', 'content')                  # Searchable fields
    list_filter = ('created_at',)                         # Filter by date

admin.site.register(BlogPost, BlogPostAdmin)  # Register model with admin
