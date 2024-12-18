# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
def home(request):
    CustomUser = get_user_model()  # Retrieve the actual model
    recent_users = CustomUser.objects.order_by('-date_joined')[:5]
    return render(request, 'home.html', {'recent_users': recent_users})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'register.html', {
        'user_form': user_form,
    })

from django.shortcuts import render
from .forms import ContactForm

def profile(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


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

def api_posts(request):
    posts = Post.objects.values("id", "title", "content")
    return JsonResponse(list(posts), safe=False)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content)
            return JsonResponse({'message': 'Post created successfully'}, status=201)
        return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def update_post(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            title = request.POST.get('title', post.title)
            content = request.POST.get('content', post.content)
            post.title = title
            post.content = content
            post.save()
            return JsonResponse({'message': 'Post updated successfully'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_post(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

