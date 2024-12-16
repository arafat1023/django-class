from django.contrib import admin
from .models import Post, UserProfile  # Ensure correct imports for the models

# Admin interface for Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at')  # Fields for Post
    search_fields = ('title', 'content')  # Searchable fields

# Admin interface for UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_image')  # Fields for UserProfile
    search_fields = ('user__username', 'bio')  # Allow search by related User model
