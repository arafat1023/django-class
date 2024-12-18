from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL maps to the home view
    path('register/', views.register, name='register'),  # Registration page path
    path('contact/', views.contact, name='contact'),
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/create-post/', views.create_post, name='create_post'),
    path('api/update-post/<int:post_id>/', views.update_post, name='update_post'),
    path('api/delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
]
