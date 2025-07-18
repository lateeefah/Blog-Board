from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()              # Main content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp

    def __str__(self):
        return self.title  # Display title in admin panel
