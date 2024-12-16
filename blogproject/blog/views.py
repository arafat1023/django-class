# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.models import User

def home(request):
    recent_users = User.objects.order_by('-date_joined')[:5]  # Fetch the 5 most recent users.
    return render(request, 'home.html', {'recent_users': recent_users})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')  # Get the uploaded file

            # Log or process the file (for demonstration purposes)
            if attachment:
                print(f"Received file: {attachment.name}")

            # Placeholder for additional processing like saving to the database or sending an email
            print(f"Received message from {name} ({email}): {message}")

            return render(request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

