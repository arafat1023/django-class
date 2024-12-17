# Django Project Setup - Comprehensive Guide

This document provides step-by-step instructions for installing Python, setting up a virtual environment, installing Django, creating a project, and configuring it for a comprehensive class demonstration.

---

## **1. Install Python**

1. **Check if Python is Already Installed**:
   Open a terminal (Linux/Mac) or Command Prompt (Windows) and run:
   ```bash
   python --version
   ```
   or:
   ```bash
   python3 --version
   ```
   If Python is installed, it will display the version number.

2. **Download Python**:
   If Python is not installed, download the latest version from the [official Python website](https://www.python.org/downloads/).

3. **Install Python**:
   - **Windows**:
     - Run the installer and make sure to check **"Add Python to PATH"** during installation.
   - **Mac/Linux**:
     - Use the installer for Mac or package manager (e.g., `apt` for Ubuntu):
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

4. **Verify Installation**:
   Run:
   ```bash
   python3 --version
   ```

---

## **2. Install Virtualenv**

1. **Install Virtualenv**:
   Run the following command to install it globally:
   ```bash
   pip install virtualenv
   ```

2. **Verify Installation**:
   Run:
   ```bash
   virtualenv --version
   ```

---

## **3. Set Up a Virtual Environment**

1. **Create a Project Directory**:
   ```bash
   mkdir django-tutorial
   cd django-tutorial
   ```

2. **Create the Virtual Environment**:
   ```bash
   virtualenv venv
   ```
   This creates a virtual environment in the `venv/` directory.

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

   You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

4. **Deactivate the Virtual Environment**:
   If needed, deactivate the environment using:
   ```bash
   deactivate
   ```

---

## **4. Install Django**

1. **Activate the Virtual Environment**:
   Make sure your virtual environment is active.

2. **Install Django**:
   ```bash
   pip install django
   ```

3. **Verify Installation**:
   Run:
   ```bash
   django-admin --version
   ```

4. **Save Dependencies**:
   Save the installed packages to a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

---

## **5. Create a Django Project**

1. **Start a Django Project**:
   Run:
   ```bash
   django-admin startproject blogproject .
   ```
   This creates the following structure:
   ```
   django-tutorial/
       manage.py
       blogproject/
           __init__.py
           asgi.py
           settings.py
           urls.py
           wsgi.py
   ```

2. **Run the Development Server**:
   Verify the project by running:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser. You should see the Django welcome page.

---

## **6. Create an App**

1. **What is a Django App?**
   An app is a web application that performs a specific functionality. Multiple apps together make a Django project.

2. **Create the Blog App**:
   Run:
   ```bash
   python manage.py startapp blog
   ```
   This creates the following structure:
   ```
   blog/
       __init__.py
       admin.py
       apps.py
       migrations/
           __init__.py
       models.py
       tests.py
       views.py
   ```

3. **Register the App in `settings.py`**:
   Open `blogproject/settings.py` and add `'blog',` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'blog',
   ]
   ```

---

## **7. Set Up Templates, Static, and Media Folders**

1. **Create the Folders**:
   Run:
   ```bash
   mkdir templates
   mkdir static
   mkdir media
   ```

2. **Update `settings.py`**:
   Configure these folders in `blogproject/settings.py`:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates'],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]

   STATIC_URL = '/static/'
   STATICFILES_DIRS = [BASE_DIR / 'static']

   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **Add a Base Template**:
   Create `templates/base.html`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <title>{% block title %}Blog Project{% endblock %}</title>
       <link rel="stylesheet" href="{% static 'css/styles.css' %}">
   </head>
   <body>
       <header>
           <h1>Welcome to the Blog Project</h1>
           <nav>
               <a href="{% url 'home' %}">Home</a>
               <a href="{% url 'register' %}">Register</a>
           </nav>
       </header>
       <main>
           {% block content %}{% endblock %}
       </main>
   </body>
   </html>
   ```

4. **Create a Static CSS File**:
   Create `static/css/styles.css`:
   ```css
   body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 0;
       background-color: #f9f9f9;
   }

   header {
       background: #007BFF;
       color: white;
       padding: 10px;
       text-align: center;
   }

   nav a {
       color: white;
       margin: 0 10px;
       text-decoration: none;
   }

   main {
       padding: 20px;
   }
   ```

---

## **8. Create Views, URLs, and Templates**

### **Home View**:
1. **Define the Home View**:
   Add this to `blog/views.py`:
   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')
   ```

2. **Map the URL**:
   Add this to `blog/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
   ```

3. **Update the Project URLs**:
   Include the `blog` app in `blogproject/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('blog.urls')),
   ]
   ```

4. **Create the Template**:
   Add `templates/home.html`:
   ```html
   {% extends 'base.html' %}

   {% block title %}Home{% endblock %}

   {% block content %}
       <h2>Welcome to the Blog!</h2>
       <p>This is the homepage.</p>
   {% endblock %}
   ```

---

## **9. Run the Server**

Start the development server:
```bash
python manage.py runserver
```

## **9. Set up Tkinter as per Tkinter.md**

Go to gui directory:
```bash
python gui_main.py
```

Visit:
- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

