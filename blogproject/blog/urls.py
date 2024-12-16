from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL maps to the home view
    path('register/', views.register, name='register'),  # Registration page path
    path('contact/', views.contact, name='contact'),
]
