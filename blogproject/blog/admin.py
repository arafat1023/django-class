from django.contrib import admin
from .models import Post, Category, Tag, CustomUser


# Admin interface for UserProfile model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "bio")
    search_fields = ("username", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "category")
    search_fields = ("title", "content")
    list_filter = ("category", "tags", "created_at")
    filter_horizontal = ("tags",)  # Makes tag selection easier
