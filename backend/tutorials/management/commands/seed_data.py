from django.core.management.base import BaseCommand
from tutorials.models import Topic, Lesson

TOPICS = [
    # ================================================================
    # TOPIC 1: GETTING STARTED
    # ================================================================
    {
        "title": "Getting Started",
        "slug": "getting-started",
        "description": "Install Django, understand its architecture, and build your first project",
        "icon": "🚀",
        "order": 1,
        "lessons": [
            {
                "title": "What is Django?",
                "slug": "what-is-django",
                "difficulty": "beginner",
                "order": 1,
                "content": '''# What is Django?

Django is a **high-level Python web framework** that encourages rapid development and clean, pragmatic design. It was created in 2003 by Adrian Holovaty and Simon Willison while working at a newspaper — built for speed, deadlines, and perfection.

## Django's Core Philosophy

> "The web framework for perfectionists with deadlines."

Django follows three guiding principles:

- **DRY (Don't Repeat Yourself)** — Every piece of logic lives in one place
- **Batteries Included** — Admin panel, ORM, auth, forms — all built-in
- **Explicit over Implicit** — Code should be readable and obvious

## The MTV Architecture

Django uses **MTV** (not MVC):

| Layer | Responsibility | Django Component |
|-------|---------------|-----------------|
| **Model** | Data structure & database | `models.py` |
| **Template** | HTML presentation | `.html` files |
| **View** | Business logic | `views.py` |

The **URL dispatcher** (`urls.py`) routes requests to the right view.

## Request/Response Lifecycle

* Browser Request
* ↓
* `urls.py` (URL routing)
* ↓
* `views.py` (Business logic)
* ↓
* `models.py` (Database query)
* ↓
* `template` (HTML rendering)
* ↓
* Browser Response

## Who Uses Django?

| Company | Use Case |
|---------|----------|
| **Instagram** | Largest Django deployment (1B+ users) |
| **Pinterest** | Discovery platform |
| **Disqus** | Comment platform (500M users) |
| **Mozilla** | Firefox websites |
| **Washington Post** | News CMS |
| **Spotify** | Backend services |

## Django vs Flask vs FastAPI

| Feature | Django | Flask | FastAPI |
|---------|--------|-------|---------|
| Type | Full-stack | Micro | Modern API |
| Admin | Built-in | ❌ | ❌ |
| ORM | Built-in | ❌ | ❌ |
| Auth | Built-in | ❌ | ❌ |
| Speed | Fast | Faster | Fastest |
| Best for | Full apps | Small apps | APIs |

---

> 💡 Django is the right choice when you need a **complete, secure, scalable web application** with minimal setup.
''',
                "code_example": '''# Django request/response cycle simulation
# Run this to understand how Django processes requests

class Request:
    def __init__(self, method, path, data=None):
        self.method = method
        self.path = path
        self.POST = data or {}
        self.user = None

class Response:
    def __init__(self, content, status=200):
        self.content = content
        self.status_code = status
    def __repr__(self):
        return f"Response({self.status_code}): {self.content[:60]}"

# URL Dispatcher (urls.py)
URL_PATTERNS = {}
def route(path):
    def decorator(func):
        URL_PATTERNS[path] = func
        return func
    return decorator

# Views (views.py)
@route("/")
def homepage(request):
    return Response("<h1>Welcome to Django!</h1>")

@route("/about/")
def about(request):
    return Response("<h1>About Us</h1><p>Built with Django</p>")

@route("/posts/")
def post_list(request):
    posts = ["Django Intro", "ORM Guide", "REST APIs"]
    html = "<ul>" + "".join(f"<li>{p}</li>" for p in posts) + "</ul>"
    return Response(html)

# URL Dispatcher
def dispatch(request):
    view = URL_PATTERNS.get(request.path)
    if view:
        return view(request)
    return Response("404 Not Found", status=404)

# Simulate incoming requests
requests = [
    Request("GET", "/"),
    Request("GET", "/about/"),
    Request("GET", "/posts/"),
    Request("GET", "/missing/"),
]

print("Django Request/Response Cycle Simulation")
print("=" * 45)
for req in requests:
    response = dispatch(req)
    print(f"  {req.method} {req.path}")
    print(f"  --> {response}")
    print()
'''
            },
            {
                "title": "Installation & First Project",
                "slug": "installation-first-project",
                "difficulty": "beginner",
                "order": 2,
                "content": '''# Installation & First Project

## System Requirements

- Python 3.10 or higher
- pip (comes with Python)
- A terminal/command prompt

Check Python:
```bash
python --version   # Python 3.11+
pip --version      # pip 23+
```

## Step 1: Virtual Environment

Always isolate your project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\\activate

# You'll see (venv) in your prompt
(venv) $
```

## Step 2: Install Django

```bash
pip install django

# Verify
django-admin --version
# 4.2.7
```

## Step 3: Create a Project

```bash
django-admin startproject mysite
cd mysite
```

### Project Structure:
```
mysite/
├── manage.py              ← Your command-line tool
└── mysite/
    ├── __init__.py
    ├── settings.py        ← ALL configuration
    ├── urls.py            ← Root URL routing
    ├── asgi.py            ← Async server entry
    └── wsgi.py            ← Production server entry
```

## Step 4: Run Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** — you'll see the Django rocket! 🚀

```bash
# Custom port
python manage.py runserver 8080

# All network interfaces (for LAN access)
python manage.py runserver 0.0.0.0:8000
```

## Step 5: Create Your First App

Django projects contain **apps** (independent modules):

```bash
python manage.py startapp blog
```

```
blog/
├── __init__.py
├── admin.py        ← Admin registration
├── apps.py         ← App configuration
├── models.py       ← Database models
├── tests.py        ← Tests
├── views.py        ← View functions
└── migrations/     ← Database migrations
    └── __init__.py
```

Register in `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    'blog',  # ← Add your app
]
```

## Essential Commands Cheatsheet

```bash
# Project & Apps
django-admin startproject <name>    # New project
python manage.py startapp <name>    # New app

# Database
python manage.py makemigrations     # Create migrations
python manage.py migrate            # Apply migrations
python manage.py dbshell            # Open DB shell

# Development
python manage.py runserver          # Dev server
python manage.py shell              # Python shell with Django
python manage.py check              # Check for errors

# Admin
python manage.py createsuperuser    # Create admin user
python manage.py collectstatic      # Gather static files

# Testing
python manage.py test               # Run tests
```

---

> 💡 **Convention:** A Django **project** is the whole website. **Apps** are pluggable components (blog, shop, users). One app should do one thing well.
''',
                "code_example": '''# Simulating Django project structure and startup
# This shows what manage.py does under the hood

import os
import sys

class DjangoProject:
    def __init__(self, name):
        self.name = name
        self.apps = []
        self.settings = {
            "DEBUG": True,
            "DATABASES": "sqlite3",
            "INSTALLED_APPS": [
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
            ]
        }

    def startapp(self, app_name):
        app = {
            "name": app_name,
            "files": ["models.py", "views.py", "admin.py", "tests.py", "apps.py"]
        }
        self.apps.append(app)
        self.settings["INSTALLED_APPS"].append(app_name)
        print(f"  Created app: '{app_name}'")
        print(f"  Files: {', '.join(app['files'])}")

    def status(self):
        print(f"Project: {self.name}")
        print(f"Apps: {len(self.apps)}")
        print(f"Debug: {self.settings['DEBUG']}")
        print(f"Database: {self.settings['DATABASES']}")
        print(f"Installed apps ({len(self.settings['INSTALLED_APPS'])}):")
        for app in self.settings["INSTALLED_APPS"]:
            print(f"  - {app}")

    def runserver(self, port=8000):
        print(f"Starting development server at http://127.0.0.1:{port}/")
        print("Quit the server with CTRL-BREAK.")

project = DjangoProject("mysite")

print("=== django-admin startproject mysite ===")
print(f"Project '{project.name}' created!")
print()

print("=== python manage.py startapp blog ===")
project.startapp("blog")
print()

print("=== python manage.py startapp users ===")
project.startapp("users")
print()

print("=== Project Status ===")
project.status()
print()

project.runserver()
'''
            },
            {
                "title": "Django Settings Deep Dive",
                "slug": "django-settings",
                "difficulty": "beginner",
                "order": 3,
                "content": '''# Django Settings Deep Dive

`settings.py` is the control center of your Django project. Let's explore every important setting.

## Core Settings

```python
# settings.py

# Security key — keep this SECRET in production!
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Debug mode — ALWAYS False in production
DEBUG = True

# Allowed hostnames in production
ALLOWED_HOSTS = ['*']  # Dev only!
# ALLOWED_HOSTS = ['mysite.com', 'www.mysite.com']  # Production
```

## Installed Apps

```python
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',          # Admin panel
    'django.contrib.auth',           # Authentication
    'django.contrib.contenttypes',   # Content types framework
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static file management

    # Your apps
    'blog',
    'users',

    # Third-party
    'rest_framework',
    'corsheaders',
]
```

## Database Configuration

```python
# SQLite (default — great for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL (recommended for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}
```

## Static & Media Files

```python
# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic output
STATICFILES_DIRS = [BASE_DIR / 'static']  # Extra static dirs

# User-uploaded media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Templates

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates
        'APP_DIRS': True,  # Look in app/templates/ folders
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
```

## Email Settings

```python
# Console backend (dev — prints to terminal)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SMTP (production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'you@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'no-reply@mysite.com'
```

## Internationalization

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'   # Indian Standard Time
USE_I18N = True               # Internationalization
USE_TZ = True                 # Timezone-aware datetimes
```

## Environment Variables (Best Practice)

Never hardcode secrets! Use `.env` files:

```bash
pip install python-dotenv
```

```python
# settings.py
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
DATABASE_URL = os.environ.get('DATABASE_URL')
```

```bash
# .env file (never commit this!)
SECRET_KEY=your-super-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

---

> ⚠️ **Production Checklist:** `DEBUG=False`, proper `ALLOWED_HOSTS`, strong `SECRET_KEY`, PostgreSQL database, `HTTPS` only.
''',
                "code_example": '''# Simulating Django settings management
# Shows how settings work and best practices

import os

class Settings:
    """Simulates Django settings.py"""

    def __init__(self, env="development"):
        self.env = env
        self._configure()

    def _configure(self):
        # Core
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "dev-insecure-key-abc123")
        self.DEBUG = self.env == "development"
        self.ALLOWED_HOSTS = ["*"] if self.DEBUG else ["mysite.com", "www.mysite.com"]

        # Apps
        self.INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.staticfiles",
            "blog",
            "users",
        ]

        # Database
        if self.env == "production":
            self.DATABASE = {"ENGINE": "postgresql", "HOST": "db.mysite.com"}
        else:
            self.DATABASE = {"ENGINE": "sqlite3", "NAME": "db.sqlite3"}

        # Email
        self.EMAIL_BACKEND = (
            "console" if self.DEBUG else "smtp"
        )

        # Timezone
        self.TIME_ZONE = "Asia/Kolkata"

    def check(self):
        issues = []
        warnings = []

        if self.DEBUG and self.env == "production":
            issues.append("DEBUG=True in production!")
        if "dev-insecure-key" in self.SECRET_KEY:
            if not self.DEBUG:
                issues.append("Insecure SECRET_KEY in production!")
            else:
                warnings.append("Using insecure SECRET_KEY (OK for dev)")
        if self.ALLOWED_HOSTS == ["*"] and not self.DEBUG:
            issues.append("ALLOWED_HOSTS=['*'] in production!")

        return issues, warnings

    def display(self):
        print(f"Environment: {self.env.upper()}")
        print(f"  DEBUG:         {self.DEBUG}")
        print(f"  ALLOWED_HOSTS: {self.ALLOWED_HOSTS}")
        print(f"  DATABASE:      {self.DATABASE['ENGINE']}")
        print(f"  EMAIL:         {self.EMAIL_BACKEND}")
        print(f"  TIMEZONE:      {self.TIME_ZONE}")
        print(f"  APPS:          {len(self.INSTALLED_APPS)} installed")

# Test development settings
print("=== Development Settings ===")
dev = Settings("development")
dev.display()
issues, warnings = dev.check()
print(f"  Issues:  {issues or 'None'}")
print(f"  Warnings: {warnings}")

print()

# Test production settings
print("=== Production Settings ===")
prod = Settings("production")
prod.display()
issues, warnings = prod.check()
print(f"  Issues:  {issues or 'None'}")
print(f"  Warnings: {warnings or 'None'}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 2: MODELS & DATABASE
    # ================================================================
    {
        "title": "Models & Database",
        "slug": "models-database",
        "description": "Define data models, relationships, and master Django ORM queries",
        "icon": "🗄️",
        "order": 2,
        "lessons": [
            {
                "title": "Creating Models",
                "slug": "creating-models",
                "difficulty": "beginner",
                "order": 1,
                "content": '''# Creating Models

A **model** is a Python class that maps to a database table. Each attribute becomes a column. Django handles all SQL automatically.

## Your First Model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
```

## Complete Field Reference

### Text Fields
```python
name = models.CharField(max_length=100)       # Short text, required max_length
bio = models.TextField()                       # Unlimited text
slug = models.SlugField(unique=True)          # URL-friendly: "my-post-title"
email = models.EmailField()                   # Validates email format
url = models.URLField()                       # Validates URL format
uuid = models.UUIDField(default=uuid.uuid4)  # UUID primary key
```

### Numeric Fields
```python
age = models.IntegerField()
price = models.DecimalField(max_digits=10, decimal_places=2)
rating = models.FloatField()
count = models.PositiveIntegerField()          # Only >= 0
big = models.BigIntegerField()
```

### Date/Time Fields
```python
birthday = models.DateField()
created = models.DateTimeField(auto_now_add=True)  # Set once on create
updated = models.DateTimeField(auto_now=True)       # Updated on every save
scheduled = models.DateTimeField(null=True, blank=True)
```

### Boolean
```python
is_active = models.BooleanField(default=True)
is_premium = models.NullBooleanField()  # True/False/None
```

### File Fields
```python
avatar = models.ImageField(upload_to='avatars/')
document = models.FileField(upload_to='docs/')
```

## Field Options (kwargs)

```python
class Article(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,          # No duplicate values
        db_index=True,        # Creates DB index (faster lookups)
        verbose_name='Title', # Human-readable name in admin
        help_text='Enter article title',
    )
    content = models.TextField(
        blank=True,           # Optional in forms (empty string OK)
        null=True,            # Allow NULL in database
        default='',           # Default value
    )
    order = models.IntegerField(
        choices=[              # Dropdown in admin
            (1, 'First'),
            (2, 'Second'),
            (3, 'Third'),
        ],
        default=1,
    )
```

## Meta Class

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']          # Default sort order
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        db_table = 'blog_posts'             # Custom table name
        unique_together = ['title', 'slug'] # Composite unique constraint
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['-created_at', 'views']),
        ]
```

## Migrations

```bash
# After defining/changing models:
python manage.py makemigrations        # Detect changes, create migration files
python manage.py migrate               # Apply migrations to DB
python manage.py showmigrations        # List all migrations
python manage.py sqlmigrate blog 0001  # Show SQL for a migration
```

---

> 💡 **Django automatically adds `id`** as an auto-increment primary key to every model unless you define one yourself.
''',
                "code_example": '''# Simulating Django model field validation

class Field:
    def __init__(self, **kwargs):
        self.max_length = kwargs.get("max_length")
        self.null = kwargs.get("null", False)
        self.blank = kwargs.get("blank", False)
        self.default = kwargs.get("default")
        self.unique = kwargs.get("unique", False)
        self.choices = kwargs.get("choices")

    def validate(self, value):
        if value is None and not self.null:
            raise ValueError("This field cannot be null")
        if value == "" and not self.blank:
            raise ValueError("This field cannot be blank")
        if self.max_length and isinstance(value, str) and len(value) > self.max_length:
            raise ValueError(f"Max length is {self.max_length}, got {len(value)}")
        if self.choices:
            valid = [c[0] for c in self.choices]
            if value not in valid:
                raise ValueError(f"Invalid choice. Options: {valid}")
        return True

class CharField(Field):
    def __repr__(self):
        return f"CharField(max_length={self.max_length})"

class TextField(Field):
    def __repr__(self):
        return "TextField()"

class IntegerField(Field):
    def validate(self, value):
        super().validate(value)
        if value is not None and not isinstance(value, int):
            raise ValueError(f"Expected int, got {type(value).__name__}")
        return True

# Simulate a Post model
class PostModel:
    title = CharField(max_length=200)
    content = TextField(blank=True)
    views = IntegerField(default=0)
    status = CharField(
        max_length=20,
        choices=[("draft","Draft"),("published","Published"),("archived","Archived")]
    )

    @classmethod
    def validate_instance(cls, data):
        fields = {
            "title": cls.title,
            "content": cls.content,
            "views": cls.views,
            "status": cls.status,
        }
        errors = {}
        for name, field in fields.items():
            if name in data:
                try:
                    field.validate(data[name])
                except ValueError as e:
                    errors[name] = str(e)
        return errors

# Test with valid data
print("=== Valid Post Data ===")
valid = {"title": "Django Guide", "content": "Great content!", "views": 0, "status": "published"}
errors = PostModel.validate_instance(valid)
print(f"Errors: {errors or 'None - validation passed!'}")

print()

# Test with invalid data
print("=== Invalid Post Data ===")
invalid = {
    "title": "A" * 250,   # Too long
    "views": "not-a-number",  # Wrong type
    "status": "unknown",       # Invalid choice
}
errors = PostModel.validate_instance(invalid)
for field, error in errors.items():
    print(f"  {field}: {error}")
'''
            },
            {
                "title": "QuerySets & ORM",
                "slug": "querysets-orm",
                "difficulty": "beginner",
                "order": 2,
                "content": '''# QuerySets & Django ORM

The Django ORM lets you query your database using Python — no SQL needed!

## Creating Objects

```python
# Method 1: create() — one step
post = Post.objects.create(
    title="My First Post",
    content="Hello Django!",
    is_published=True
)

# Method 2: save() — two steps
post = Post(title="My Post", content="Content")
post.save()

# Method 3: get_or_create() — prevent duplicates
post, created = Post.objects.get_or_create(
    title="Unique Post",
    defaults={"content": "Default content"}
)
print(created)  # True if newly created, False if existed
```

## Reading Objects

```python
# All objects
Post.objects.all()

# One object — raises DoesNotExist if not found
Post.objects.get(id=1)
Post.objects.get(title="My Post")

# Filter — returns QuerySet (multiple)
Post.objects.filter(is_published=True)
Post.objects.filter(views__gt=100)

# Exclude
Post.objects.exclude(is_published=True)

# First / Last
Post.objects.first()
Post.objects.last()
Post.objects.order_by('created_at').first()

# Count
Post.objects.count()
Post.objects.filter(is_published=True).count()

# Exists (fast!)
Post.objects.filter(title="test").exists()  # True/False
```

## Field Lookups (Filters)

```python
# Exact (default)
filter(title="Hello")
filter(title__exact="Hello")

# Case-insensitive
filter(title__iexact="hello")
filter(title__icontains="django")

# Starts/ends with
filter(title__startswith="My")
filter(title__endswith="Guide")

# Numeric comparisons
filter(views__gt=100)    # greater than
filter(views__gte=100)   # greater than or equal
filter(views__lt=10)     # less than
filter(views__lte=10)    # less than or equal

# Range
filter(views__range=(100, 1000))
filter(created_at__date=date.today())
filter(created_at__year=2024)
filter(created_at__month=6)

# In a list
filter(id__in=[1, 2, 3, 4])
filter(status__in=["published", "featured"])

# Null checks
filter(content__isnull=True)
filter(content__isnull=False)
```

## Updating Objects

```python
# Update one
post = Post.objects.get(id=1)
post.title = "Updated Title"
post.save()

# Update specific fields only (efficient!)
post.save(update_fields=['title'])

# Bulk update — single SQL UPDATE
Post.objects.filter(is_published=False).update(is_published=True)
Post.objects.all().update(views=0)
```

## Deleting Objects

```python
# Delete one
post = Post.objects.get(id=1)
post.delete()

# Delete filtered queryset
Post.objects.filter(views=0).delete()

# Delete all
Post.objects.all().delete()  # ⚠️ Careful!
```

## Chaining, Ordering, Slicing

```python
# Chain filters
Post.objects \
    .filter(is_published=True) \
    .filter(views__gt=100) \
    .order_by('-created_at') \
    .exclude(title__startswith='Draft')

# Multiple ordering
Post.objects.order_by('-views', 'title')  # views DESC, title ASC

# Slicing (LIMIT/OFFSET)
Post.objects.all()[:10]        # First 10
Post.objects.all()[10:20]      # Next 10
Post.objects.order_by('-views')[0]  # Most viewed

# Distinct
Post.objects.values('author').distinct()
```

## Aggregation

```python
from django.db.models import Count, Sum, Avg, Max, Min

Post.objects.aggregate(total=Count('id'))
Post.objects.aggregate(avg_views=Avg('views'))
Post.objects.aggregate(
    total=Count('id'),
    max_views=Max('views'),
    avg_views=Avg('views')
)

# Group by (annotate)
from django.db.models import Count
authors = Author.objects.annotate(post_count=Count('post'))
for author in authors:
    print(author.name, author.post_count)
```

---

> 💡 **QuerySets are lazy** — they don't hit the database until you evaluate them (iterate, slice, call `list()`, `len()`, etc.)
''',
                "code_example": '''# Complete Django ORM operations simulation
from datetime import datetime, timedelta

class QuerySet:
    def __init__(self, data):
        self._data = list(data)

    def filter(self, **kwargs):
        result = list(self._data)
        for key, value in kwargs.items():
            parts = key.split("__")
            field = parts[0]
            op = parts[1] if len(parts) > 1 else "exact"

            if op == "exact":
                result = [r for r in result if r.get(field) == value]
            elif op == "icontains":
                result = [r for r in result if value.lower() in str(r.get(field,"")).lower()]
            elif op == "gt":
                result = [r for r in result if r.get(field, 0) > value]
            elif op == "gte":
                result = [r for r in result if r.get(field, 0) >= value]
            elif op == "lt":
                result = [r for r in result if r.get(field, 0) < value]
            elif op == "in":
                result = [r for r in result if r.get(field) in value]
            elif op == "startswith":
                result = [r for r in result if str(r.get(field,"")).startswith(value)]
        return QuerySet(result)

    def exclude(self, **kwargs):
        included = self.filter(**kwargs)._data
        excluded = [r for r in self._data if r not in included]
        return QuerySet(excluded)

    def order_by(self, field):
        rev = field.startswith("-")
        key = field.lstrip("-")
        return QuerySet(sorted(self._data, key=lambda x: x.get(key, 0), reverse=rev))

    def count(self): return len(self._data)
    def first(self): return self._data[0] if self._data else None
    def last(self): return self._data[-1] if self._data else None
    def exists(self): return len(self._data) > 0
    def all(self): return QuerySet(self._data)
    def __getitem__(self, s): return QuerySet(self._data[s]) if isinstance(s, slice) else self._data[s]
    def __iter__(self): return iter(self._data)
    def __repr__(self): return f"<QuerySet [{len(self._data)} objects]>"

class Manager:
    def __init__(self, data): self._data = data
    def all(self): return QuerySet(self._data)
    def filter(self, **kw): return QuerySet(self._data).filter(**kw)
    def exclude(self, **kw): return QuerySet(self._data).exclude(**kw)
    def get(self, **kw):
        result = list(self.filter(**kw))
        if len(result) == 1: return result[0]
        elif len(result) == 0: raise Exception("DoesNotExist")
        raise Exception("MultipleObjectsReturned")

# Sample database
posts_db = [
    {"id":1, "title":"Intro to Django", "views":1500, "is_published":True, "status":"published"},
    {"id":2, "title":"Django ORM Guide", "views":900, "is_published":True, "status":"published"},
    {"id":3, "title":"Draft Post", "views":0, "is_published":False, "status":"draft"},
    {"id":4, "title":"Advanced Django", "views":2100, "is_published":True, "status":"published"},
    {"id":5, "title":"Django REST API", "views":750, "is_published":True, "status":"published"},
    {"id":6, "title":"My Django Notes", "views":50, "is_published":False, "status":"draft"},
]

Post = Manager(posts_db)

print("=== Basic Queries ===")
print("All posts:", Post.all())
print("Published:", Post.filter(is_published=True))
print("Views > 1000:", Post.filter(views__gt=1000))
print("Contains 'django':", Post.filter(title__icontains="django"))

print()
print("=== Chained Queries ===")
result = Post.filter(is_published=True).filter(views__gt=500).order_by("-views")
print("Published + Popular:", result)

print()
print("=== get() ===")
try:
    post = Post.get(id=1)
    print("Found:", post["title"])
except Exception as e:
    print("Error:", e)

print()
print("=== Top 3 by views ===")
top3 = Post.all().order_by("-views")[:3]
for p in top3:
    print(f"  #{p['id']} {p['title']} - {p['views']} views")
'''
            },
            {
                "title": "Model Relationships",
                "slug": "model-relationships",
                "difficulty": "intermediate",
                "order": 3,
                "content": '''# Model Relationships

Real applications have related data. Django supports three types of relationships.

## ForeignKey (One-to-Many)

One author → many posts:

```python
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,      # Delete posts if user deleted
        related_name='posts',          # user.posts.all()
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,     # Keep post if category deleted
        null=True, blank=True,
        related_name='posts',
    )
    title = models.CharField(max_length=200)
```

Usage:
```python
user = User.objects.get(id=1)
user.posts.all()              # All posts by this user
user.posts.filter(is_published=True)
user.posts.count()

post.author.username          # Access author from post
post.category.name            # Access category from post
```

## ManyToManyField

Posts ↔ Tags (a post has many tags, a tag belongs to many posts):

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
```

Usage:
```python
post = Post.objects.get(id=1)
tag = Tag.objects.get(name='python')

post.tags.add(tag)            # Add a tag
post.tags.remove(tag)         # Remove a tag
post.tags.clear()             # Remove all tags
post.tags.all()               # Get all tags
post.tags.set([tag1, tag2])   # Replace all tags

# Reverse — posts with 'python' tag
tag.posts.all()
```

## ManyToMany with Extra Fields (Through Model)

When you need extra data on the relationship:

```python
class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(
        User,
        through='Enrollment',
        related_name='courses'
    )

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
```

## OneToOneField

Each user has exactly one profile:

```python
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

user.profile.bio              # Access profile
user.profile.avatar.url
```

## on_delete Options

```python
# CASCADE — delete related objects too (most common)
author = models.ForeignKey(User, on_delete=models.CASCADE)

# PROTECT — raise error if related objects exist
category = models.ForeignKey(Category, on_delete=models.PROTECT)

# SET_NULL — set FK to NULL
manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

# SET_DEFAULT — set FK to default value
status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)

# DO_NOTHING — database handles it (dangerous!)
# SET — set to a custom value or callable
```

## Optimizing Queries: N+1 Problem

```python
# BAD — N+1 queries (1 for posts + 1 per post for author)
posts = Post.objects.all()
for post in posts:
    print(post.author.username)  # Extra query each time!

# GOOD — select_related (JOIN for ForeignKey/OneToOne)
posts = Post.objects.select_related('author', 'category').all()

# GOOD — prefetch_related (for ManyToMany)
posts = Post.objects.prefetch_related('tags').all()

# Combine both
posts = Post.objects \
    .select_related('author', 'category') \
    .prefetch_related('tags') \
    .all()
```

---

> 💡 **Always use `select_related` and `prefetch_related`** when accessing related objects in loops to avoid the N+1 query problem.
''',
                "code_example": '''# Simulating Django model relationships

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"User({self.name})"

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"Category({self.name})"

class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"Tag({self.name})"

class Post:
    def __init__(self, id, title, author, category=None):
        self.id = id
        self.title = title
        self.author = author        # ForeignKey
        self.category = category    # ForeignKey
        self.tags = []              # ManyToMany

    def add_tag(self, *tags):
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)

    def __repr__(self):
        return f"Post('{self.title}')"

# Create objects
alice = User(1, "Alice")
bob = User(2, "Bob")

python_cat = Category(1, "Python")
web_cat = Category(2, "Web Development")

py_tag = Tag(1, "python")
django_tag = Tag(2, "django")
api_tag = Tag(3, "api")
beginner_tag = Tag(4, "beginner")

# Posts with relationships
posts = [
    Post(1, "Intro to Django", alice, python_cat),
    Post(2, "Django ORM Deep Dive", alice, python_cat),
    Post(3, "Building REST APIs", bob, web_cat),
    Post(4, "Flask vs Django", bob, web_cat),
]

posts[0].add_tag(py_tag, django_tag, beginner_tag)
posts[1].add_tag(py_tag, django_tag)
posts[2].add_tag(django_tag, api_tag)
posts[3].add_tag(py_tag)

# === ForeignKey queries ===
print("=== ForeignKey (One-to-Many) ===")
alices_posts = [p for p in posts if p.author.id == alice.id]
print(f"Alice's posts: {alices_posts}")

python_posts = [p for p in posts if p.category and p.category.id == python_cat.id]
print(f"Python category: {python_posts}")

# === ManyToMany queries ===
print()
print("=== ManyToMany ===")
print(f"Tags on '{posts[0].title}': {posts[0].tags}")

django_posts = [p for p in posts if django_tag in p.tags]
print(f"Posts with 'django' tag: {django_posts}")

# === N+1 problem demo ===
print()
print("=== N+1 Problem Demo ===")
print("BAD (would fire extra queries):")
for post in posts:
    print(f"  - {post.title} by {post.author.name} in {post.category.name if post.category else 'None'}")

print()
print("GOOD (with select_related - single JOIN query):")
print("  In Django: Post.objects.select_related('author','category').all()")
print("  Result: Same output but only 1 SQL query instead of", len(posts)+1)
'''
            },
            {
                "title": "Advanced ORM - Annotations & Aggregations",
                "slug": "advanced-orm",
                "difficulty": "advanced",
                "order": 4,
                "content": '''# Advanced ORM — Annotations & Aggregations

## Aggregation Functions

```python
from django.db.models import (
    Count, Sum, Avg, Max, Min, F, Q, Value,
    Case, When, IntegerField, CharField
)

# Single aggregation
Post.objects.aggregate(total=Count('id'))
# {'total': 42}

# Multiple at once
Post.objects.aggregate(
    total=Count('id'),
    published=Count('id', filter=Q(is_published=True)),
    avg_views=Avg('views'),
    max_views=Max('views'),
    total_views=Sum('views'),
)
```

## Annotation (Add Computed Fields)

```python
# Add post count to each author
from django.contrib.auth.models import User

authors = User.objects.annotate(
    post_count=Count('posts'),
    published_count=Count('posts', filter=Q(posts__is_published=True)),
    total_views=Sum('posts__views'),
)

for author in authors:
    print(f"{author.username}: {author.post_count} posts, {author.total_views} views")
```

## F Expressions (Reference DB Fields)

```python
from django.db.models import F

# Increment views without reading (atomic!)
Post.objects.filter(id=1).update(views=F('views') + 1)

# Compare two fields
Post.objects.filter(likes__gt=F('dislikes'))  # More likes than dislikes
Post.objects.filter(updated_at__gt=F('created_at'))
```

## Q Objects (Complex Filtering)

```python
from django.db.models import Q

# OR condition
Post.objects.filter(Q(title__icontains='django') | Q(title__icontains='python'))

# AND (default, but explicit)
Post.objects.filter(Q(is_published=True) & Q(views__gt=100))

# NOT
Post.objects.filter(~Q(status='draft'))

# Complex nested
Post.objects.filter(
    Q(is_published=True) &
    (Q(views__gt=1000) | Q(featured=True)) &
    ~Q(status='archived')
)
```

## Values & Values List

```python
# Return dictionaries instead of model instances
Post.objects.values('id', 'title', 'views')
# [{'id': 1, 'title': 'Post 1', 'views': 100}, ...]

# Return flat tuples
Post.objects.values_list('id', 'title')
# [(1, 'Post 1'), (2, 'Post 2'), ...]

# Single flat list
Post.objects.values_list('title', flat=True)
# ['Post 1', 'Post 2', ...]

# Unique titles
Post.objects.values_list('title', flat=True).distinct()
```

## Raw SQL (Last Resort)

```python
# Raw SQL query
posts = Post.objects.raw('SELECT * FROM blog_post WHERE views > %s', [100])

# Completely custom SQL
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("UPDATE blog_post SET views = views + 1 WHERE id = %s", [post_id])
    cursor.execute("SELECT COUNT(*) FROM blog_post")
    row = cursor.fetchone()
```

## Case/When (Conditional Expressions)

```python
from django.db.models import Case, When, Value, CharField

posts = Post.objects.annotate(
    popularity=Case(
        When(views__gte=10000, then=Value('Viral')),
        When(views__gte=1000, then=Value('Popular')),
        When(views__gte=100, then=Value('Normal')),
        default=Value('Unknown'),
        output_field=CharField(),
    )
)

for post in posts:
    print(f"{post.title}: {post.popularity}")
```

## Subqueries

```python
from django.db.models import OuterRef, Subquery

# Get the latest post title for each author
latest_post = Post.objects.filter(
    author=OuterRef('pk')
).order_by('-created_at').values('title')[:1]

authors = Author.objects.annotate(
    latest_post_title=Subquery(latest_post)
)
```

---

> 💡 Use `django-debug-toolbar` in development to see exactly what SQL queries are being fired — it's the best tool for ORM optimization.
''',
                "code_example": '''# Simulating Django aggregation and annotation

# Simulated database
posts = [
    {"id":1,"title":"Intro to Django","views":1500,"likes":120,"author":"alice","published":True},
    {"id":2,"title":"ORM Guide","views":900,"likes":80,"author":"alice","published":True},
    {"id":3,"title":"Draft Post","views":0,"likes":0,"author":"alice","published":False},
    {"id":4,"title":"Advanced Django","views":2100,"likes":200,"author":"bob","published":True},
    {"id":5,"title":"REST APIs","views":750,"likes":60,"author":"bob","published":True},
    {"id":6,"title":"Django Admin","views":3200,"likes":310,"author":"charlie","published":True},
    {"id":7,"title":"Testing Django","views":450,"likes":35,"author":"charlie","published":True},
    {"id":8,"title":"My Notes","views":20,"likes":2,"author":"charlie","published":False},
]

def aggregate(qs, **funcs):
    result = {}
    for name, fn in funcs.items():
        result[name] = fn(qs)
    return result

def count(qs): return len(qs)
def avg_views(qs): return round(sum(p["views"] for p in qs) / len(qs), 1) if qs else 0
def max_views(qs): return max(p["views"] for p in qs) if qs else 0
def sum_views(qs): return sum(p["views"] for p in qs)

# === Aggregate ===
print("=== Post.objects.aggregate() ===")
published = [p for p in posts if p["published"]]
stats = aggregate(
    published,
    total=count,
    max_views=max_views,
    avg_views=avg_views,
    total_views=sum_views,
)
for k, v in stats.items():
    print(f"  {k}: {v}")

# === Annotate (group by author) ===
print()
print("=== Author.objects.annotate(post_count, total_views) ===")
from collections import defaultdict
author_stats = defaultdict(lambda: {"posts": 0, "total_views": 0, "published": 0})
for post in posts:
    a = post["author"]
    author_stats[a]["posts"] += 1
    author_stats[a]["total_views"] += post["views"]
    if post["published"]:
        author_stats[a]["published"] += 1

for author, stats in sorted(author_stats.items()):
    print(f"  {author}: {stats['posts']} posts, {stats['published']} published, {stats['total_views']} total views")

# === Q Objects (OR/AND/NOT) ===
print()
print("=== Complex Q Filtering ===")

# Q(views__gt=1000) | Q(likes__gt=150)
popular = [p for p in posts if p["views"] > 1000 or p["likes"] > 150]
print(f"Popular (views>1000 OR likes>150): {[p['title'] for p in popular]}")

# ~Q(published=True) = drafts
drafts = [p for p in posts if not p["published"]]
print(f"Drafts (~published): {[p['title'] for p in drafts]}")

# === Case/When ===
print()
print("=== Popularity Labels (Case/When) ===")
for post in sorted(posts, key=lambda x: -x["views"]):
    if post["views"] >= 2000:
        label = "Viral"
    elif post["views"] >= 1000:
        label = "Popular"
    elif post["views"] >= 100:
        label = "Normal"
    else:
        label = "Low"
    print(f"  {post['title'][:25]:25} → {label} ({post['views']} views)")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 3: VIEWS & URLS
    # ================================================================
    {
        "title": "Views & URLs",
        "slug": "views-urls",
        "description": "Handle HTTP requests with function and class-based views",
        "icon": "🔗",
        "order": 3,
        "lessons": [
            {
                "title": "URL Routing",
                "slug": "url-routing",
                "difficulty": "beginner",
                "order": 1,
                "content": '''# URL Routing

Django's URL dispatcher maps URLs to view functions. It's defined in `urls.py` files.

## Basic URL Patterns

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),       # Include app URLs
    path('users/', include('users.urls')),
    path('api/', include('api.urls')),
]
```

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('<slug:slug>/', views.post_by_slug, name='post-slug'),
    path('new/', views.post_create, name='post-create'),
    path('<int:pk>/edit/', views.post_edit, name='post-edit'),
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),
]
```

## URL Converters

```python
# int — positive integer
path('post/<int:pk>/', view)           # /post/42/

# str — non-empty string, excluding /
path('user/<str:username>/', view)     # /user/alice/

# slug — letters, numbers, hyphens, underscores
path('post/<slug:slug>/', view)        # /post/my-first-post/

# uuid — UUID format
path('item/<uuid:uuid>/', view)        # /item/075194d3-6885.../

# path — any string including /
path('files/<path:filepath>/', view)   # /files/docs/report.pdf/
```

## Named URL Patterns

```python
# Define
path('post/<int:pk>/', views.post_detail, name='post-detail')

# Use in view
from django.urls import reverse
url = reverse('post-detail', kwargs={'pk': 1})
# '/blog/post/1/'

# Use in template
<a href="{% url 'post-detail' pk=post.pk %}">View Post</a>

# Use in redirect
return redirect('post-detail', pk=new_post.pk)
```

## URL Namespaces

Organize URLs by app to avoid name conflicts:

```python
# blog/urls.py
app_name = 'blog'   # ← namespace

urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:pk>/', views.post_detail, name='detail'),
]
```

Usage:
```python
# In view
reverse('blog:detail', kwargs={'pk': 1})

# In template
{% url 'blog:detail' pk=post.pk %}
```

## Regular Expressions (re_path)

```python
from django.urls import re_path

urlpatterns = [
    # Match /archive/2024/01/
    re_path(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.archive),

    # Match /tag/python/ or /tag/django-rest/
    re_path(r'^tag/(?P<slug>[-\\w]+)/$', views.tag_detail),
]
```

## Include with Namespace

```python
# mysite/urls.py
urlpatterns = [
    path('blog/', include(('blog.urls', 'blog'))),
    path('shop/', include(('shop.urls', 'shop'))),
]
```

## Static & Media Files in Development

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

> 💡 Always name your URL patterns with `name=`. It lets you change URLs later without breaking templates or views.
''',
                "code_example": '''# URL routing simulation

import re

class URLPattern:
    def __init__(self, pattern, view_name, name=None):
        self.pattern = pattern
        self.view_name = view_name
        self.name = name
        # Convert Django-style patterns to regex
        regex = pattern
        regex = re.sub(r"<int:(\\w+)>",  lambda m: f"(?P<{m.group(1)}>[0-9]+)", regex)
        regex = re.sub(r"<slug:(\\w+)>", lambda m: f"(?P<{m.group(1)}>[-a-zA-Z0-9_]+)", regex)
        regex = re.sub(r"<str:(\\w+)>",  lambda m: f"(?P<{m.group(1)}>[^/]+)", regex)
        self.regex = "^" + regex + "$"

    def match(self, path):
        m = re.match(self.regex, path)
        if m:
            return m.groupdict()
        return None

    def __repr__(self):
        return f"path('{self.pattern}', name='{self.name}')"

class URLResolver:
    def __init__(self, prefix="", patterns=None):
        self.prefix = prefix
        self.patterns = patterns or []

    def include(self, prefix, patterns):
        for p in patterns:
            p.pattern = prefix + p.pattern
            p.regex = "^" + prefix + p.pattern.lstrip("^").rstrip("$") + "$"
        self.patterns.extend(patterns)

    def resolve(self, path):
        for pattern in self.patterns:
            kwargs = pattern.match(path)
            if kwargs is not None:
                return pattern.view_name, kwargs
        return None, {}

    def reverse(self, name, **kwargs):
        for p in self.patterns:
            if p.name == name:
                result = p.pattern
                for k, v in kwargs.items():
                    result = re.sub(rf"<[^:]*:{k}>", str(v), result)
                    result = re.sub(rf"<{k}>", str(v), result)
                return result
        raise Exception(f"No URL named '{name}'")

# Define URL patterns
blog_urls = [
    URLPattern("", "post_list", name="post-list"),
    URLPattern("<int:pk>/", "post_detail", name="post-detail"),
    URLPattern("<slug:slug>/", "post_by_slug", name="post-slug"),
    URLPattern("new/", "post_create", name="post-create"),
    URLPattern("<int:pk>/edit/", "post_edit", name="post-edit"),
]

resolver = URLResolver()
for p in blog_urls:
    p.pattern = "blog/" + p.pattern
    p.regex = "^blog/" + p.pattern[len("blog/"):]
resolver.patterns = blog_urls

# Test URL resolution
test_paths = [
    "blog/",
    "blog/42/",
    "blog/my-django-post/",
    "blog/new/",
    "blog/42/edit/",
    "shop/products/",  # Should not match
]

print("=== URL Resolution ===")
for path in test_paths:
    view, kwargs = resolver.resolve(path)
    if view:
        print(f"  /{path} -> view='{view}' kwargs={kwargs}")
    else:
        print(f"  /{path} -> 404 Not Found")

print()
print("=== reverse() — URL by name ===")
names = [
    ("post-list", {}),
    ("post-detail", {"pk": 42}),
    ("post-slug", {"slug": "my-django-post"}),
    ("post-edit", {"pk": 7}),
]
for name, kwargs in names:
    try:
        url = resolver.reverse(name, **kwargs)
        print(f"  reverse('{name}', {kwargs}) -> /{url}")
    except Exception as e:
        print(f"  ERROR: {e}")
'''
            },
            {
                "title": "Function-Based Views",
                "slug": "function-based-views",
                "difficulty": "beginner",
                "order": 2,
                "content": '''# Function-Based Views (FBVs)

A view is a Python function that takes an `HttpRequest` and returns an `HttpResponse`.

## Basic View

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'title': 'All Posts',
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/post_detail.html', {'post': post})
```

## Handling GET and POST

```python
from django.contrib import messages

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if not title:
            messages.error(request, 'Title is required!')
            return render(request, 'blog/create.html')

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        messages.success(request, 'Post created!')
        return redirect('post-detail', pk=post.pk)

    # GET request
    return render(request, 'blog/create.html')
```

## Useful Decorators

```python
from django.views.decorators.http import (
    require_GET, require_POST, require_http_methods
)
from django.contrib.auth.decorators import (
    login_required, permission_required
)
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

# Only allow GET
@require_GET
def homepage(request):
    return HttpResponse("Home")

# Only allow POST
@require_POST
def submit_form(request):
    return HttpResponse("Submitted")

# Require login
@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

# Require permission
@permission_required('blog.can_publish')
def publish_post(request, pk):
    pass

# Cache for 15 minutes
@cache_page(60 * 15)
def expensive_view(request):
    pass

# Stack multiple decorators (bottom-up execution)
@login_required
@require_http_methods(["GET", "POST"])
def create_post(request):
    pass
```

## JSON API Views

```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def post_list_json(request):
    posts = Post.objects.filter(is_published=True).values(
        'id', 'title', 'views', 'created_at'
    )
    return JsonResponse({'posts': list(posts)})

@csrf_exempt
def post_create_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    try:
        data = json.loads(request.body)
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
        )
        return JsonResponse({'id': post.id, 'title': post.title}, status=201)
    except (KeyError, json.JSONDecodeError) as e:
        return JsonResponse({'error': str(e)}, status=400)
```

## Pagination

```python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    all_posts = Post.objects.filter(is_published=True)
    paginator = Paginator(all_posts, 10)  # 10 posts per page

    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)

    return render(request, 'blog/list.html', {
        'page_obj': page_obj,
        'is_paginated': paginator.num_pages > 1,
    })
```

```html
<!-- Template pagination -->
{% if is_paginated %}
    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">← Previous</a>
    {% endif %}
    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next →</a>
    {% endif %}
{% endif %}
```

---

> 💡 Use `get_object_or_404()` instead of `.get()` — it automatically returns a 404 response instead of crashing with a 500 error.
''',
                "code_example": '''# Function-Based View simulation

class HttpRequest:
    def __init__(self, method="GET", path="/", post_data=None, user=None):
        self.method = method
        self.path = path
        self.POST = post_data or {}
        self.GET = {}
        self.user = user
        self._messages = []

class HttpResponse:
    def __init__(self, content, status=200, content_type="text/html"):
        self.content = content
        self.status_code = status
        self.content_type = content_type
    def __repr__(self):
        return f"HttpResponse({self.status_code})"

class Http404(Exception):
    pass

# Database simulation
posts_db = {
    1: {"id":1,"title":"Django Basics","content":"Learn Django...","published":True,"views":150},
    2: {"id":2,"title":"Advanced ORM","content":"QuerySets...","published":True,"views":300},
    3: {"id":3,"title":"Draft Post","content":"Not ready...","published":False,"views":0},
}

def get_object_or_404(model, **kwargs):
    pk = kwargs.get("pk") or kwargs.get("id")
    obj = model.get(pk) if pk else None
    if not obj:
        raise Http404(f"Not found: {kwargs}")
    for k, v in kwargs.items():
        if k in ("pk","id"): continue
        if k == "published" and obj.get("published") != v:
            raise Http404("Not found")
    return obj

def render(request, template, context={}):
    data = f"[{template}] " + ", ".join(f"{k}={repr(v)[:30]}" for k,v in context.items())
    return HttpResponse(data)

def redirect(url_name, pk=None):
    url = f"/{url_name}/{pk}/" if pk else f"/{url_name}/"
    resp = HttpResponse(f"Redirecting to {url}", status=302)
    return resp

# === Views ===
def post_list(request):
    posts = [p for p in posts_db.values() if p["published"]]
    posts.sort(key=lambda x: -x["views"])
    return render(request, "blog/list.html", {"posts": posts, "count": len(posts)})

def post_detail(request, pk):
    try:
        post = get_object_or_404(posts_db, pk=pk, published=True)
        posts_db[pk]["views"] += 1
        return render(request, "blog/detail.html", {"post": post})
    except Http404 as e:
        return HttpResponse(str(e), status=404)

def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            return render(request, "blog/create.html", {"error": "Title required"})
        new_id = max(posts_db.keys()) + 1
        post = {"id": new_id, "title": title, "content": "", "published": False, "views": 0}
        posts_db[new_id] = post
        return redirect("post-detail", pk=new_id)
    return render(request, "blog/create.html", {})

# Simulate requests
print("=== GET /blog/ ===")
print(post_list(HttpRequest("GET", "/blog/")))

print()
print("=== GET /blog/2/ ===")
print(post_detail(HttpRequest("GET", "/blog/2/"), pk=2))
print(f"  Views incremented: {posts_db[2]['views']}")

print()
print("=== GET /blog/999/ (not found) ===")
print(post_detail(HttpRequest("GET", "/blog/999/"), pk=999))

print()
print("=== GET /blog/3/ (unpublished) ===")
print(post_detail(HttpRequest("GET", "/blog/3/"), pk=3))

print()
print("=== POST /blog/new/ (valid) ===")
req = HttpRequest("POST", "/blog/new/", post_data={"title": "New Post!"})
print(post_create(req))

print()
print("=== POST /blog/new/ (invalid) ===")
req2 = HttpRequest("POST", "/blog/new/", post_data={"title": ""})
print(post_create(req2))
'''
            },
            {
                "title": "Class-Based Views",
                "slug": "class-based-views",
                "difficulty": "intermediate",
                "order": 3,
                "content": '''# Class-Based Views (CBVs)

Django's generic CBVs eliminate boilerplate. One class = full CRUD functionality.

## Generic Views Overview

```python
from django.views.generic import (
    TemplateView,                      # Static pages
    ListView, DetailView,              # Read
    CreateView, UpdateView, DeleteView # Write
    FormView, RedirectView
)
```

## ListView

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Default: blog/post_list.html
    context_object_name = 'posts'          # Default: object_list
    paginate_by = 10                       # Automatic pagination!

    def get_queryset(self):
        """Filter based on URL params or user"""
        qs = Post.objects.filter(is_published=True)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        """Add extra context"""
        context = super().get_context_data(**kwargs)
        context['total_count'] = Post.objects.count()
        return context
```

## DetailView

```python
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'        # URL field (default: pk)
    slug_url_kwarg = 'slug'    # URL kwarg name

    def get_object(self):
        obj = super().get_object()
        # Increment view count
        Post.objects.filter(pk=obj.pk).update(views=F('views')+1)
        return obj
```

## CreateView

```python
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'category', 'is_published']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.author = self.request.user   # Auto-set author
        return super().form_valid(form)
```

## UpdateView

```python
from django.contrib.auth.mixins import UserPassesTestMixin

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_published']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only author can edit

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})
```

## DeleteView

```python
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user == self.get_object().author
```

## URLs for CBVs

```python
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]
```

## Common Mixins

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin,       # Require authentication
    PermissionRequiredMixin,  # Require specific permission
    UserPassesTestMixin,      # Custom test function
)

class SecureView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'blog.view_post'
    login_url = '/accounts/login/'
    raise_exception = True  # 403 instead of redirect
```

## FBV vs CBV Comparison

| Task | FBV | CBV |
|------|-----|-----|
| List all posts | ~15 lines | 4 lines |
| Show one post | ~10 lines | 3 lines |
| Create post | ~25 lines | 6 lines |
| Update post | ~25 lines | 6 lines |
| Delete post | ~15 lines | 5 lines |
| **Total** | **~90 lines** | **~24 lines** |

---

> 💡 Use CBVs for standard CRUD. Use FBVs for complex custom logic where the class hierarchy adds confusion.
''',
                "code_example": '''# Class-Based View simulation

# Base model
posts_db = [
    {"id":1,"title":"Django CBVs","content":"Class-based views are powerful.","published":True,"views":200,"author":"alice"},
    {"id":2,"title":"ORM Guide","content":"Master QuerySets.","published":True,"views":450,"author":"alice"},
    {"id":3,"title":"Draft","content":"Work in progress.","published":False,"views":0,"author":"bob"},
    {"id":4,"title":"REST APIs","content":"Build APIs with DRF.","published":True,"views":320,"author":"bob"},
]

class BaseView:
    model = posts_db

    def get_queryset(self):
        return list(self.model)

    def as_view(self):
        return self  # Simplified

class ListView(BaseView):
    context_object_name = "objects"
    paginate_by = None

    def get(self, request=None):
        qs = self.get_queryset()
        context = {self.context_object_name: qs}
        return {"template": "list.html", "context": context}

class DetailView(BaseView):
    def get(self, request=None, pk=None):
        obj = next((p for p in self.model if p["id"] == pk), None)
        if not obj:
            return {"error": "404 Not Found"}
        return {"template": "detail.html", "context": {"object": obj}}

class CreateView(BaseView):
    fields = []

    def post(self, data, request=None):
        # Validate required fields
        for f in self.fields:
            if not data.get(f):
                return {"error": f"Field '{f}' is required"}
        new_id = max(p["id"] for p in self.model) + 1
        obj = {"id": new_id, **{f: data.get(f, "") for f in self.fields}, "views": 0}
        self.model.append(obj)
        return {"redirect": f"/post/{new_id}/", "object": obj}

class UpdateView(BaseView):
    fields = []

    def post(self, pk, data, request=None):
        obj = next((p for p in self.model if p["id"] == pk), None)
        if not obj:
            return {"error": "Not Found"}
        for f in self.fields:
            if f in data:
                obj[f] = data[f]
        return {"redirect": f"/post/{pk}/", "object": obj}

class DeleteView(BaseView):
    def post(self, pk, request=None):
        obj = next((p for p in self.model if p["id"] == pk), None)
        if not obj:
            return {"error": "Not Found"}
        self.model.remove(obj)
        return {"redirect": "/posts/", "deleted": obj["title"]}

# Define concrete views (just like in Django!)
class PostListView(ListView):
    context_object_name = "posts"
    def get_queryset(self):
        return [p for p in super().get_queryset() if p["published"]]

class PostDetailView(DetailView):
    def get(self, request=None, pk=None):
        result = super().get(pk=pk)
        if "object" in result.get("context", {}):
            result["context"]["object"]["views"] += 1
        return result

class PostCreateView(CreateView):
    fields = ["title", "content", "author"]

class PostUpdateView(UpdateView):
    fields = ["title", "content", "published"]

class PostDeleteView(DeleteView):
    pass

# === Demo ===
print("=== ListView ===")
view = PostListView()
result = view.get()
print(f"Template: {result['template']}")
print(f"Posts: {[p['title'] for p in result['context']['posts']]}")

print()
print("=== DetailView ===")
view = PostDetailView()
result = view.get(pk=2)
print(f"Post: {result['context']['object']['title']} (views: {result['context']['object']['views']})")

print()
print("=== CreateView ===")
view = PostCreateView()
result = view.post({"title": "New Post", "content": "Content here", "author": "charlie"})
print(f"Created: {result['object']}")

print()
print("=== UpdateView ===")
view = PostUpdateView()
result = view.post(2, {"title": "ORM Mastery Guide", "published": True})
print(f"Updated: {result['object']['title']}")

print()
print("=== DeleteView ===")
view = PostDeleteView()
result = view.post(3)
print(f"Deleted: {result['deleted']}")
print(f"Remaining: {len(posts_db)} posts")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 4: TEMPLATES
    # ================================================================
    {
        "title": "Templates",
        "slug": "templates",
        "description": "Build dynamic HTML with Django's powerful template engine",
        "icon": "🎨",
        "order": 4,
        "lessons": [
            {
                "title": "Template Basics",
                "slug": "template-basics",
                "difficulty": "beginner",
                "order": 1,
                "content": '''# Template Basics

Django's template language is designed to be easy for designers while powerful for developers.

## Template Syntax

### Variables `{{ }}`

```html
<h1>{{ post.title }}</h1>
<p>Author: {{ post.author.username }}</p>
<p>Views: {{ post.views }}</p>
<p>Date: {{ post.created_at }}</p>
```

### Tags `{% %}`

```html
<!-- If/Else -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% elif user.is_staff %}
    <p>Staff user</p>
{% else %}
    <a href="/login/">Login</a>
{% endif %}

<!-- For loop -->
{% for post in posts %}
    <article>
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    </article>
{% empty %}
    <p>No posts yet.</p>
{% endfor %}

<!-- Loop variables -->
{% for item in items %}
    {{ forloop.counter }}     {# 1, 2, 3... #}
    {{ forloop.counter0 }}    {# 0, 1, 2... #}
    {{ forloop.last }}        {# True on last item #}
    {{ forloop.first }}       {# True on first item #}
{% endfor %}

<!-- URL tag -->
<a href="{% url 'blog:detail' pk=post.pk %}">Read more</a>

<!-- Static files -->
{% load static %}
<img src="{% static 'images/logo.png' %}">
<link rel="stylesheet" href="{% static 'css/main.css' %}">
```

### Filters `|`

```html
{{ post.title|upper }}              <!-- TITLE -->
{{ post.title|lower }}              <!-- title -->
{{ post.title|capfirst }}           <!-- Title -->
{{ post.title|truncatechars:50 }}   <!-- Truncate to 50 chars -->
{{ post.title|truncatewords:10 }}   <!-- Truncate to 10 words -->
{{ post.content|linebreaks }}       <!-- Convert newlines to <p> -->
{{ post.content|striptags }}        <!-- Remove HTML tags -->
{{ post.content|safe }}             <!-- Mark as safe (no escaping) -->
{{ post.views|default:"0" }}        <!-- Fallback if empty -->
{{ post.created_at|date:"F j, Y" }} <!-- "January 5, 2024" -->
{{ post.created_at|timesince }}     <!-- "3 days ago" -->
{{ price|floatformat:2 }}           <!-- 19.99 -->
{{ items|length }}                  <!-- Count items -->
{{ items|first }}                   <!-- First item -->
{{ items|last }}                    <!-- Last item -->
{{ text|wordcount }}                <!-- Word count -->
```

## Template Inheritance

`base.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'blog:list' %}">Blog</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>© 2024 My Site</footer>
    {% block scripts %}{% endblock %}
</body>
</html>
```

`blog/post_list.html`:
```html
{% extends 'base.html' %}

{% block title %}Blog Posts{% endblock %}

{% block content %}
<h1>Latest Posts</h1>
{% for post in posts %}
    <article>
        <h2><a href="{% url 'blog:detail' pk=post.pk %}">{{ post.title }}</a></h2>
        <p>{{ post.content|truncatewords:30 }}</p>
        <small>{{ post.created_at|date:"M d, Y" }} | {{ post.views }} views</small>
    </article>
{% empty %}
    <p>No posts yet.</p>
{% endfor %}
{% endblock %}
```

## Template Includes

```html
<!-- Reusable components -->
{% include 'components/navbar.html' %}
{% include 'components/post_card.html' with post=post %}
{% include 'components/pagination.html' with page_obj=page_obj %}
```

## Custom Template Tags & Filters

```python
# blog/templatetags/blog_extras.py
from django import template
from ..models import Post

register = template.Library()

@register.filter
def reading_time(content):
    words = len(content.split())
    minutes = max(1, words // 200)
    return f"{minutes} min read"

@register.simple_tag
def get_popular_posts(count=5):
    return Post.objects.filter(is_published=True).order_by('-views')[:count]

@register.inclusion_tag('components/post_card.html')
def post_card(post):
    return {'post': post}
```

Usage:
```html
{% load blog_extras %}
<small>{{ post.content|reading_time }}</small>

{% get_popular_posts as popular %}
{% for post in popular %}
    <a href="...">{{ post.title }}</a>
{% endfor %}
```

---

> 💡 Django auto-escapes HTML in templates to prevent XSS attacks. Use `|safe` only for trusted content.
''',
                "code_example": '''# Django template engine simulation

class Template:
    def __init__(self, source):
        self.source = source

    def render(self, context={}):
        result = self.source

        # {{ variable }} - simple variable replacement
        import re
        def replace_var(match):
            expr = match.group(1).strip()
            parts = expr.split("|")
            var_path = parts[0].strip()
            filters = [f.strip() for f in parts[1:]]

            # Resolve dotted paths
            value = context
            for part in var_path.split("."):
                if isinstance(value, dict):
                    value = value.get(part, "")
                else:
                    value = getattr(value, part, "")

            # Apply filters
            for f in filters:
                if f == "upper":
                    value = str(value).upper()
                elif f == "lower":
                    value = str(value).lower()
                elif f == "capfirst":
                    value = str(value).capitalize()
                elif f.startswith("truncatewords:"):
                    n = int(f.split(":")[1])
                    words = str(value).split()
                    value = " ".join(words[:n]) + ("..." if len(words) > n else "")
                elif f.startswith("default:"):
                    if not value:
                        value = f.split(":", 1)[1].strip('"').strip("'")

            return str(value)

        result = re.sub(r"\{\{(.*?)\}\}", replace_var, result)

        # {% if %} basic support
        def process_if(text, ctx):
            pattern = r"\{%\s*if\s+(\\w+)\s*%\}(.*?)\{%\s*endif\s*%\}"
            def replace_if(m):
                var, block = m.group(1), m.group(2)
                val = ctx.get(var)
                if "{% else %}" in block:
                    then_block, else_block = block.split("{% else %}")
                else:
                    then_block, else_block = block, ""
                return then_block.strip() if val else else_block.strip()
            return re.sub(pattern, replace_if, text, flags=re.DOTALL)

        # {% for %} basic support
        def process_for(text, ctx):
            pattern = r"\{%\s*for\s+(\\w+)\s+in\s+(\\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}"
            def replace_for(m):
                item_name, list_name, body = m.group(1), m.group(2), m.group(3)
                items = ctx.get(list_name, [])
                if not items:
                    return ""
                rendered = []
                for i, item in enumerate(items):
                    item_ctx = {**ctx, item_name: item,
                                "forloop": {"counter": i+1, "first": i==0, "last": i==len(items)-1}}
                    part = re.sub(r"\{\{(.*?)\}\}",
                        lambda m2, ic=item_ctx: replace_var.__wrapped__(m2) if False
                        else str(ic.get(m2.group(1).strip(), "")), body)
                    rendered.append(part)
                return "".join(rendered)
            return re.sub(pattern, replace_for, text, flags=re.DOTALL)

        result = process_if(result, context)

        # Simple for loop
        import re
        for_match = re.search(r"\{%\s*for\s+(\\w+)\s+in\s+(\\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}", result, re.DOTALL)
        if for_match:
            item_name, list_name, body = for_match.group(1), for_match.group(2), for_match.group(3)
            items = context.get(list_name, [])
            rendered_items = []
            for i, item in enumerate(items):
                row = body
                for k, v in (item.items() if isinstance(item, dict) else {}):
                    row = row.replace("{{ " + item_name + "." + k + " }}", str(v))
                    row = row.replace("{{" + item_name + "." + k + "}}", str(v))
                row = row.replace("{{ forloop.counter }}", str(i+1))
                rendered_items.append(row)
            result = result[:for_match.start()] + "".join(rendered_items) + result[for_match.end():]

        return result.strip()

# Test the template engine
template_source = """
Blog - {{ site_name }}
{{ user_greeting }}
Latest Posts ({{ post_count }} total):
{% for post in posts %}  #{{ forloop.counter }} {{ post.title }} - {{ post.views }} views
{% endfor %}
"""

posts = [
    {"title": "Intro to Django", "views": 1500},
    {"title": "ORM Mastery", "views": 900},
    {"title": "REST APIs", "views": 750},
]

context = {
    "site_name": "DjangoLearn",
    "user_greeting": "Welcome back, Alice!",
    "post_count": len(posts),
    "posts": posts,
}

t = Template(template_source)
print(t.render(context))

# Test filters
print("=== Filter Tests ===")
filter_tests = [
    Template("{{ title|upper }}").render({"title": "hello world"}),
    Template("{{ title|capfirst }}").render({"title": "hello world"}),
    Template("{{ text|truncatewords:4 }}").render({"text": "Django is a high level Python web framework"}),
    Template("{{ value|default:'N/A' }}").render({"value": ""}),
]
for r in filter_tests:
    print(f"  {r}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 5: FORMS
    # ================================================================
    {
        "title": "Forms",
        "slug": "forms",
        "description": "Handle user input with Django Forms and ModelForms",
        "icon": "📝",
        "order": 5,
        "lessons": [
            {
                "title": "Django Forms",
                "slug": "django-forms",
                "difficulty": "intermediate",
                "order": 1,
                "content": '''# Django Forms

Django forms handle validation, rendering, and processing of user input.

## Creating a Form

```python
# blog/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        min_length=20,
    )
    subject = forms.ChoiceField(choices=[
        ('general', 'General Inquiry'),
        ('support', 'Technical Support'),
        ('billing', 'Billing'),
    ])
    subscribe = forms.BooleanField(required=False)
```

## Processing in Views

```python
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Access cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Contact from {name}",
                message=message,
                from_email=email,
                recipient_list=['admin@mysite.com'],
            )
            return redirect('contact-success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

## ModelForm (Best for DB Models)

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'is_published']
        # OR: exclude = ['author', 'created_at']
        # OR: fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title...'}),
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'is_published': 'Publish now?'
        }
        help_texts = {
            'title': 'Keep it under 200 characters',
        }
```

## Custom Validation

```python
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    # Validate a single field
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken!")
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters.")
        return username.lower()  # Normalize

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    # Validate multiple fields together
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data
```

## Template Rendering

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}

    <!-- Render all fields -->
    {{ form.as_p }}
    <!-- or {{ form.as_table }} or {{ form.as_ul }} -->

    <!-- Manual rendering -->
    <div class="mb-3">
        <label for="{{ form.title.id_for_label }}">{{ form.title.label }}</label>
        {{ form.title }}
        {% if form.title.errors %}
            <div class="error">{{ form.title.errors }}</div>
        {% endif %}
        {% if form.title.help_text %}
            <small>{{ form.title.help_text }}</small>
        {% endif %}
    </div>

    <!-- Non-field errors -->
    {{ form.non_field_errors }}

    <button type="submit">Submit</button>
</form>
```

## Widgets Reference

```python
forms.TextInput()          # <input type="text">
forms.PasswordInput()      # <input type="password">
forms.EmailInput()         # <input type="email">
forms.NumberInput()        # <input type="number">
forms.Textarea()           # <textarea>
forms.Select()             # <select>
forms.CheckboxInput()      # <input type="checkbox">
forms.RadioSelect()        # Radio buttons
forms.FileInput()          # <input type="file">
forms.DateInput()          # <input type="date">
forms.HiddenInput()        # <input type="hidden">
forms.SelectMultiple()     # Multi-select
forms.SplitDateTimeWidget()# Date + time split inputs
```

---

> 💡 Always include `{% csrf_token %}` in forms. Django rejects POST requests without it to prevent CSRF attacks.
''',
                "code_example": '''# Django Forms validation simulation

class ValidationError(Exception):
    pass

class Field:
    def __init__(self, required=True, **kwargs):
        self.required = required
        self.kwargs = kwargs

    def validate(self, value):
        if self.required and not value and value != 0:
            raise ValidationError("This field is required.")
        return value

class CharField(Field):
    def validate(self, value):
        value = super().validate(value)
        max_length = self.kwargs.get("max_length")
        min_length = self.kwargs.get("min_length", 0)
        if value:
            if max_length and len(str(value)) > max_length:
                raise ValidationError(f"Max {max_length} characters (got {len(str(value))})")
            if len(str(value)) < min_length:
                raise ValidationError(f"Min {min_length} characters")
        return str(value).strip() if value else value

class EmailField(CharField):
    def validate(self, value):
        value = super().validate(value)
        if value and "@" not in value:
            raise ValidationError("Enter a valid email address.")
        return value.lower() if value else value

class IntegerField(Field):
    def validate(self, value):
        value = super().validate(value)
        if value:
            try:
                int_val = int(value)
                min_val = self.kwargs.get("min_value")
                max_val = self.kwargs.get("max_value")
                if min_val is not None and int_val < min_val:
                    raise ValidationError(f"Must be >= {min_val}")
                if max_val is not None and int_val > max_val:
                    raise ValidationError(f"Must be <= {max_val}")
                return int_val
            except (TypeError, ValueError):
                raise ValidationError("Enter a valid integer.")
        return value

class Form:
    def __init__(self, data=None):
        self.data = data or {}
        self._errors = {}
        self.cleaned_data = {}
        self._is_bound = data is not None

    @property
    def fields(self):
        return {
            name: field for name, field in self.__class__.__dict__.items()
            if isinstance(field, Field)
        }

    def is_valid(self):
        if not self._is_bound:
            return False
        self._errors = {}
        self.cleaned_data = {}
        for name, field in self.fields.items():
            value = self.data.get(name)
            try:
                clean_method = getattr(self, f"clean_{name}", None)
                cleaned = field.validate(value)
                if clean_method:
                    cleaned = clean_method(cleaned)
                self.cleaned_data[name] = cleaned
            except ValidationError as e:
                self._errors[name] = str(e)
        try:
            self.clean()
        except ValidationError as e:
            self._errors["__all__"] = str(e)
        return len(self._errors) == 0

    def clean(self):
        pass

    def errors(self):
        return self._errors

# Contact Form
class ContactForm(Form):
    name = CharField(max_length=100, min_length=2)
    email = EmailField()
    message = CharField(min_length=10, max_length=1000)
    age = IntegerField(min_value=13, max_value=120, required=False)

    def clean_name(self, value):
        if value and any(c.isdigit() for c in value):
            raise ValidationError("Name should not contain numbers.")
        return value.title()  # Capitalize each word

# Registration Form
class RegistrationForm(Form):
    username = CharField(max_length=30, min_length=3)
    email = EmailField()
    password = CharField(min_length=8)
    password_confirm = CharField(min_length=8)

    def clean(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password_confirm")
        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords do not match!")

print("=== ContactForm (Valid) ===")
form = ContactForm({
    "name": "alice smith",
    "email": "alice@example.com",
    "message": "I love Django tutorials!",
    "age": "25",
})
print(f"Valid: {form.is_valid()}")
print(f"Cleaned data: {form.cleaned_data}")

print()
print("=== ContactForm (Invalid) ===")
form2 = ContactForm({"name": "A", "email": "not-an-email", "message": "short"})
print(f"Valid: {form2.is_valid()}")
for field, error in form2.errors().items():
    print(f"  {field}: {error}")

print()
print("=== RegistrationForm (Password Mismatch) ===")
form3 = RegistrationForm({
    "username": "alice",
    "email": "alice@example.com",
    "password": "securepass123",
    "password_confirm": "wrongpass",
})
print(f"Valid: {form3.is_valid()}")
for field, error in form3.errors().items():
    print(f"  {field}: {error}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 6: AUTHENTICATION
    # ================================================================
    {
        "title": "Authentication & Authorization",
        "slug": "authentication",
        "description": "Secure your app with Django's complete auth system",
        "icon": "🔐",
        "order": 6,
        "lessons": [
            {
                "title": "Authentication System",
                "slug": "auth-system",
                "difficulty": "intermediate",
                "order": 1,
                "content": '''# Django Authentication System

Django ships with a complete authentication system covering users, groups, and permissions.

## Custom User Model (Always Do This First!)

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)   # Make email unique
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    website = models.URLField(blank=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'       # Login with email instead of username
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'  # Must be set BEFORE first migration!
```

## Registration

```python
# accounts/forms.py
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cd = super().clean()
        if cd.get('password1') != cd.get('password2'):
            raise forms.ValidationError("Passwords don't match")
        return cd

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Hash password!
        if commit:
            user.save()
        return user
```

```python
# accounts/views.py
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after register
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
```

## Protecting Views

```python
# Function-based
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

# Class-based
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
```

## Permissions

```python
# Check permissions
request.user.has_perm('blog.add_post')      # Can create posts
request.user.has_perm('blog.change_post')   # Can edit posts
request.user.has_perm('blog.delete_post')   # Can delete posts

# Grant permissions
from django.contrib.auth.models import Permission
perm = Permission.objects.get(codename='publish_post')
user.user_permissions.add(perm)

# Groups
from django.contrib.auth.models import Group
editors = Group.objects.get(name='Editors')
user.groups.add(editors)

# Custom permission on model
class Post(models.Model):
    class Meta:
        permissions = [
            ('publish_post', 'Can publish posts'),
            ('feature_post', 'Can feature posts'),
        ]
```

## Password Management

```python
# Change password
user.set_password('new_secure_password')
user.save()

# Check password
user.check_password('input_password')  # True/False

# Built-in password reset URLs
# Add to urls.py:
path('accounts/', include('django.contrib.auth.urls')),
# Provides:
# /accounts/password_change/
# /accounts/password_reset/
# /accounts/password_reset/done/
# /accounts/reset/<uidb64>/<token>/
```

## User in Templates

```html
{% if user.is_authenticated %}
    <a href="/logout/">Logout {{ user.username }}</a>
    {% if user.is_staff %}
        <a href="/admin/">Admin</a>
    {% endif %}
{% else %}
    <a href="/login/">Login</a>
    <a href="/register/">Register</a>
{% endif %}
```

---

> ⚠️ **Critical:** Always set `AUTH_USER_MODEL` before your first migration. Changing it later requires database surgery.
''',
                "code_example": '''# Django Authentication System Simulation
import hashlib, os, re
from datetime import datetime

class AuthUser:
    def __init__(self, id, username, email, password_hash, is_active=True, is_staff=False):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.is_active = is_active
        self.is_staff = is_staff
        self.is_authenticated = False
        self.permissions = set()
        self.groups = set()
        self.date_joined = datetime.now()

    @staticmethod
    def hash_password(password):
        salt = os.urandom(16).hex()
        h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000)
        return f"pbkdf2${salt}${h.hex()}"

    def check_password(self, password):
        _, salt, stored = self.password_hash.split("$")
        h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000)
        return h.hex() == stored

    def has_perm(self, perm):
        return perm in self.permissions

    def __repr__(self):
        return f"User({self.email}, auth={self.is_authenticated})"

class AuthBackend:
    users = {}
    sessions = {}

    @classmethod
    def create_user(cls, username, email, password):
        # Validate
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password too short (min 8 chars)")
        if email in [u.email for u in cls.users.values()]:
            raise ValueError("Email already registered")

        uid = len(cls.users) + 1
        user = AuthUser(uid, username, email, AuthUser.hash_password(password))
        cls.users[uid] = user
        print(f"  Created user: {email}")
        return user

    @classmethod
    def authenticate(cls, email, password):
        user = next((u for u in cls.users.values() if u.email == email), None)
        if user and user.check_password(password) and user.is_active:
            return user
        return None

    @classmethod
    def login(cls, user):
        session_key = os.urandom(16).hex()
        user.is_authenticated = True
        cls.sessions[session_key] = user.id
        print(f"  Login OK: {user.email} (session={session_key[:8]}...)")
        return session_key

    @classmethod
    def logout(cls, session_key):
        uid = cls.sessions.pop(session_key, None)
        if uid and uid in cls.users:
            cls.users[uid].is_authenticated = False
            print(f"  Logged out user id={uid}")

    @classmethod
    def get_user_from_session(cls, session_key):
        uid = cls.sessions.get(session_key)
        return cls.users.get(uid)

print("=== User Registration ===")
try:
    alice = AuthBackend.create_user("alice", "alice@example.com", "secret123!")
    bob = AuthBackend.create_user("bob", "bob@example.com", "mypass456!")
except ValueError as e:
    print(f"Error: {e}")

# Duplicate email
try:
    AuthBackend.create_user("alice2", "alice@example.com", "test1234!")
except ValueError as e:
    print(f"Duplicate email error: {e}")

print()
print("=== Authentication ===")

# Correct credentials
user = AuthBackend.authenticate("alice@example.com", "secret123!")
if user:
    session = AuthBackend.login(user)
    print(f"  Authenticated: {user}")

    # Access control
    user.permissions.add("blog.add_post")
    user.permissions.add("blog.change_post")
    print(f"  has_perm(add_post): {user.has_perm('blog.add_post')}")
    print(f"  has_perm(delete_post): {user.has_perm('blog.delete_post')}")

print()

# Wrong password
user2 = AuthBackend.authenticate("alice@example.com", "wrongpass")
print(f"Wrong password auth result: {user2}")

print()
print("=== Session Management ===")
retrieved_user = AuthBackend.get_user_from_session(session)
print(f"User from session: {retrieved_user.email}")

AuthBackend.logout(session)
retrieved_after_logout = AuthBackend.get_user_from_session(session)
print(f"After logout: {retrieved_after_logout}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 7: DJANGO REST FRAMEWORK
    # ================================================================
    {
        "title": "Django REST Framework",
        "slug": "django-rest-framework",
        "description": "Build professional REST APIs with DRF",
        "icon": "⚡",
        "order": 7,
        "lessons": [
            {
                "title": "DRF Serializers",
                "slug": "drf-serializers",
                "difficulty": "intermediate",
                "order": 1,
                "content": '''# DRF Serializers

Serializers convert complex data (model instances, querysets) to Python dicts → JSON, and validate incoming data.

## Installation

```bash
pip install djangorestframework
```

```python
INSTALLED_APPS = ['rest_framework']
```

## Basic Serializer

```python
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    views = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
```

## ModelSerializer (Most Common)

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'views', 'is_published', 'created_at']
        read_only_fields = ['id', 'created_at', 'views']

# Nested serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created_at']

class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)       # Nested
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comment_count(self, obj):
        return obj.comments.count()
```

## Custom Fields & Validation

```python
class PostSerializer(serializers.ModelSerializer):
    # Custom computed field
    reading_time = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.username', read_only=True)
    tag_names = serializers.StringRelatedField(many=True, source='tags')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_name', 'tag_names',
                  'reading_time', 'is_published']

    def get_reading_time(self, obj):
        words = len(obj.content.split())
        return f"{max(1, words // 200)} min"

    # Field-level validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value.strip()

    # Object-level validation
    def validate(self, data):
        if data.get('is_published') and len(data.get('content', '')) < 100:
            raise serializers.ValidationError(
                "Published posts must have at least 100 characters."
            )
        return data
```

## DRF API Views

```python
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Function-based API view
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(is_published=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Generic class-based API
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ViewSet (full CRUD in one class)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
```

## DRF Authentication & Permissions

```python
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser,
    IsAuthenticatedOrReadOnly, AllowAny
)
from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication, BasicAuthentication
)

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

## Router (Auto URL Generation)

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]
# Auto-generates:
# GET/POST /api/posts/
# GET/PUT/PATCH/DELETE /api/posts/{pk}/
```

---

> 💡 DRF's **browsable API** is one of its best features — visit any API endpoint in a browser for an interactive interface.
''',
                "code_example": '''# DRF Serializer simulation
import json
from datetime import datetime

class ValidationError(Exception):
    pass

class SerializerField:
    def __init__(self, read_only=False, required=True, default=None, **kwargs):
        self.read_only = read_only
        self.required = required
        self.default = default
        self.kwargs = kwargs

    def to_representation(self, value):
        return value

    def to_internal_value(self, value):
        return value

    def validate(self, value):
        return value

class CharField(SerializerField):
    def validate(self, value):
        max_len = self.kwargs.get("max_length")
        min_len = self.kwargs.get("min_length", 0)
        if value is not None:
            if max_len and len(str(value)) > max_len:
                raise ValidationError(f"Max length is {max_len}")
            if len(str(value)) < min_len:
                raise ValidationError(f"Min length is {min_len}")
        return str(value).strip() if value else value

class IntegerField(SerializerField):
    def to_representation(self, value):
        return int(value) if value is not None else 0
    def to_internal_value(self, value):
        try: return int(value)
        except (TypeError, ValueError): raise ValidationError("Expected integer")

class BooleanField(SerializerField):
    def to_internal_value(self, value):
        if isinstance(value, bool): return value
        if str(value).lower() in ("true","1","yes"): return True
        if str(value).lower() in ("false","0","no"): return False
        raise ValidationError("Expected boolean")

class Serializer:
    def __init__(self, instance=None, data=None, many=False, **kwargs):
        self.instance = instance
        self._data = data
        self.many = many
        self._errors = {}
        self.validated_data = {}

    @property
    def fields(self):
        return {k: v for k, v in self.__class__.__dict__.items()
                if isinstance(v, SerializerField)}

    def to_representation(self, instance):
        obj = instance if isinstance(instance, dict) else vars(instance)
        result = {}
        for name, field in self.fields.items():
            result[name] = field.to_representation(obj.get(name))
        return result

    @property
    def data(self):
        if self.many:
            return [self.to_representation(item) for item in self.instance]
        return self.to_representation(self.instance)

    def is_valid(self):
        if self._data is None:
            return False
        self._errors = {}
        self.validated_data = {}
        for name, field in self.fields.items():
            if field.read_only:
                continue
            value = self._data.get(name, field.default)
            if value is None and field.required:
                self._errors[name] = "This field is required."
                continue
            try:
                value = field.to_internal_value(value)
                value = field.validate(value)
                # Custom field validator
                validator = getattr(self, f"validate_{name}", None)
                if validator:
                    value = validator(value)
                self.validated_data[name] = value
            except ValidationError as e:
                self._errors[name] = str(e)
        try:
            self.validate(self.validated_data)
        except ValidationError as e:
            self._errors["non_field_errors"] = str(e)
        return len(self._errors) == 0

    def validate(self, data):
        return data

    @property
    def errors(self):
        return self._errors

class PostSerializer(Serializer):
    title = CharField(max_length=200, min_length=3)
    content = CharField(min_length=10)
    views = IntegerField(read_only=True, default=0)
    is_published = BooleanField(default=False)

    def validate_title(self, value):
        banned = ["spam", "test123"]
        if any(b in value.lower() for b in banned):
            raise ValidationError(f"Title contains banned words: {banned}")
        return value.title()

    def validate(self, data):
        if data.get("is_published") and len(data.get("content","")) < 50:
            raise ValidationError("Published posts need 50+ chars in content")
        return data

# Test data
posts_db = [
    {"title": "Intro to Django", "content": "Django is a Python web framework...", "views": 1500, "is_published": True},
    {"title": "ORM Guide", "content": "QuerySets are lazy evaluated...", "views": 900, "is_published": True},
]

print("=== Serializing (Model -> JSON) ===")
serializer = PostSerializer(instance=posts_db, many=True)
print(json.dumps(serializer.data, indent=2))

print()
print("=== Deserializing (JSON -> Validated Data) ===")

valid_data = {"title": "new django post", "content": "This is a great tutorial about Django REST Framework.", "is_published": False}
s = PostSerializer(data=valid_data)
print(f"Valid input valid: {s.is_valid()}")
print(f"Validated: {s.validated_data}")

print()
print("=== Validation Errors ===")
invalid_data = {"title": "Hi", "content": "short", "is_published": True}
s2 = PostSerializer(data=invalid_data)
print(f"Valid: {s2.is_valid()}")
print(f"Errors: {json.dumps(s2.errors, indent=2)}")
'''
            },
            {
                "title": "DRF ViewSets & Routers",
                "slug": "drf-viewsets-routers",
                "difficulty": "intermediate",
                "order": 2,
                "content": '''# DRF ViewSets & Routers

ViewSets combine multiple views into one class. Routers auto-generate URLs.

## ViewSet Types

```python
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

# ReadOnlyModelViewSet - only GET operations
class PostReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    # Provides: list() and retrieve()

# ModelViewSet - full CRUD
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Provides: list, create, retrieve, update, partial_update, destroy

# Custom ViewSet with only specific operations
class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet   # No update or delete!
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

## Filtering, Search & Ordering

```bash
pip install django-filter
```

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Exact filtering: /api/posts/?is_published=true&category=1
    filterset_fields = ['is_published', 'category', 'author']

    # Search: /api/posts/?search=django
    search_fields = ['title', 'content', 'author__username']

    # Ordering: /api/posts/?ordering=-views
    ordering_fields = ['views', 'created_at', 'title']
    ordering = ['-created_at']  # Default ordering
```

## Custom Actions

```python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Detail action: POST /api/posts/{pk}/publish/
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def publish(self, request, pk=None):
        post = self.get_object()
        if post.author != request.user:
            return Response({'error': 'Not your post'}, status=403)
        post.is_published = True
        post.save()
        return Response({'status': 'published', 'id': post.id})

    # List action: GET /api/posts/trending/
    @action(detail=False, methods=['get'])
    def trending(self, request):
        trending = Post.objects.filter(
            is_published=True
        ).order_by('-views')[:10]
        serializer = self.get_serializer(trending, many=True)
        return Response(serializer.data)

    # Custom serializer per action
    def get_serializer_class(self):
        if self.action in ('list',):
            return PostListSerializer
        return PostDetailSerializer

    # Filter queryset per user
    def get_queryset(self):
        if self.action == 'list':
            return Post.objects.filter(is_published=True)
        return Post.objects.all()

    # Auto-set author on create
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

## Pagination

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Or per viewset
from rest_framework.pagination import PageNumberPagination, CursorPagination

class PostPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination
```

## Throttling (Rate Limiting)

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}
```

## API Response Format

```python
# Response structure
{
    "count": 42,
    "next": "http://api.example.com/posts/?page=3",
    "previous": "http://api.example.com/posts/?page=1",
    "results": [
        {
            "id": 1,
            "title": "Post title",
            "author": "alice",
            "views": 1500,
            "created_at": "2024-01-15T10:30:00Z"
        }
    ]
}
```

---

> 💡 Use `ModelViewSet` for standard CRUD and add custom `@action` decorators for extra endpoints like `/publish/`, `/like/`, `/share/`.
''',
                "code_example": '''# DRF ViewSet + Router simulation
import json

class Response:
    def __init__(self, data, status=200):
        self.data = data
        self.status = status
    def __repr__(self):
        return f"Response({self.status}): {json.dumps(self.data, default=str)[:80]}"

# Simulated database
posts_db = [
    {"id":1,"title":"Intro to Django","content":"Django basics...","views":1500,"is_published":True,"author":"alice"},
    {"id":2,"title":"ORM Guide","content":"QuerySets...","views":900,"is_published":True,"author":"alice"},
    {"id":3,"title":"Draft","content":"WIP...","views":0,"is_published":False,"author":"bob"},
    {"id":4,"title":"REST APIs","content":"Build APIs...","views":3200,"is_published":True,"author":"bob"},
    {"id":5,"title":"Testing","content":"Test everything...","views":450,"is_published":True,"author":"charlie"},
]

class Router:
    def __init__(self):
        self.routes = {}

    def register(self, prefix, viewset):
        self.routes[prefix] = viewset
        print(f"Registered routes:")
        print(f"  GET    /{prefix}/            -> {viewset.__name__}.list()")
        print(f"  POST   /{prefix}/            -> {viewset.__name__}.create()")
        print(f"  GET    /{prefix}/{{pk}}/       -> {viewset.__name__}.retrieve()")
        print(f"  PUT    /{prefix}/{{pk}}/       -> {viewset.__name__}.update()")
        print(f"  PATCH  /{prefix}/{{pk}}/       -> {viewset.__name__}.partial_update()")
        print(f"  DELETE /{prefix}/{{pk}}/       -> {viewset.__name__}.destroy()")

        # Register custom actions
        for name, method in viewset.__dict__.items():
            if hasattr(method, "_is_action"):
                detail = method._detail
                http_methods = method._methods
                url = f"  {'/'.join(m.upper() for m in http_methods):6} /{prefix}/{'{{pk}}/' if detail else ''}{name}/ -> {viewset.__name__}.{name}()"
                print(url)

def action(detail=True, methods=None):
    def decorator(func):
        func._is_action = True
        func._detail = detail
        func._methods = methods or ["get"]
        return func
    return decorator

class PostViewSet:
    db = posts_db

    @classmethod
    def list(cls, request=None, **params):
        results = [p for p in cls.db if p["is_published"]]
        # Search
        search = params.get("search")
        if search:
            results = [p for p in results if search.lower() in p["title"].lower()]
        # Ordering
        ordering = params.get("ordering", "-views")
        reverse = ordering.startswith("-")
        key = ordering.lstrip("-")
        results = sorted(results, key=lambda x: x.get(key, 0), reverse=reverse)
        return Response({"count": len(results), "results": results})

    @classmethod
    def retrieve(cls, request=None, pk=None):
        post = next((p for p in cls.db if p["id"] == pk), None)
        if not post:
            return Response({"error": "Not found"}, status=404)
        return Response(post)

    @classmethod
    def create(cls, request=None, data=None):
        if not data.get("title"):
            return Response({"title": ["This field is required."]}, status=400)
        new = {"id": max(p["id"] for p in cls.db)+1, **data, "views": 0}
        cls.db.append(new)
        return Response(new, status=201)

    @classmethod
    def destroy(cls, request=None, pk=None):
        post = next((p for p in cls.db if p["id"] == pk), None)
        if not post:
            return Response({"error": "Not found"}, status=404)
        cls.db.remove(post)
        return Response(None, status=204)

    @classmethod
    @action(detail=False, methods=["get"])
    def trending(cls, request=None):
        top = sorted([p for p in cls.db if p["is_published"]],
                     key=lambda x: -x["views"])[:3]
        return Response({"trending": top})

    @classmethod
    @action(detail=True, methods=["post"])
    def publish(cls, request=None, pk=None):
        post = next((p for p in cls.db if p["id"] == pk), None)
        if not post:
            return Response({"error": "Not found"}, status=404)
        post["is_published"] = True
        return Response({"status": "published", "title": post["title"]})

# === Register routes ===
print("=== Router Registration ===")
router = Router()
router.register("posts", PostViewSet)

print()
print("=== API Calls ===")

print("GET /posts/")
r = PostViewSet.list()
print(f"  Count: {r.data['count']}, First: {r.data['results'][0]['title']}")

print()
print("GET /posts/?search=django&ordering=-views")
r = PostViewSet.list(search="django", ordering="-views")
print(f"  Results: {[p['title'] for p in r.data['results']]}")

print()
print("GET /posts/1/")
print(PostViewSet.retrieve(pk=1))

print()
print("POST /posts/ (create)")
r = PostViewSet.create(data={"title": "New Post", "content": "Content!", "is_published": True, "author": "dave"})
print(r)

print()
print("GET /posts/trending/")
r = PostViewSet.trending()
print(f"  Trending: {[p['title'] for p in r.data['trending']]}")

print()
print("POST /posts/3/publish/")
r = PostViewSet.publish(pk=3)
print(r)

print()
print("DELETE /posts/3/")
print(PostViewSet.destroy(pk=3))
'''
            },
            {
                "title": "JWT Authentication",
                "slug": "jwt-authentication",
                "difficulty": "advanced",
                "order": 3,
                "content": '''# JWT Authentication with DRF

JWT (JSON Web Tokens) is the modern way to authenticate APIs.

## Installation

```bash
pip install djangorestframework-simplejwt
```

```python
# settings.py
INSTALLED_APPS = ['rest_framework']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT settings
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

## URL Setup

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),       # Get token
    path('api/token/refresh/', TokenRefreshView.as_view()),  # Refresh
    path('api/token/verify/', TokenVerifyView.as_view()),    # Verify
]
```

## Custom Token Claims

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to JWT payload
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
```

## Usage Flow

```bash
# 1. Obtain token
POST /api/token/
{
    "username": "alice",
    "password": "secret123"
}

# Response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}

# 2. Use access token in requests
GET /api/posts/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

# 3. Refresh when expired
POST /api/token/refresh/
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Protected Views

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })
```

## Custom Permissions

```python
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
```

---

> 💡 **Access tokens** are short-lived (minutes/hours). **Refresh tokens** are long-lived (days/weeks). Never store tokens in localStorage — use HttpOnly cookies for production.
''',
                "code_example": '''# JWT Authentication simulation
import hashlib, json, base64, hmac, time, os

class JWT:
    """Simplified JWT implementation to understand how it works"""

    @staticmethod
    def b64encode(data):
        return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b"=").decode()

    @staticmethod
    def b64decode(s):
        padding = 4 - len(s) % 4
        return json.loads(base64.urlsafe_b64decode(s + "=" * padding))

    @classmethod
    def create_token(cls, payload, secret, expires_in=3600):
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {**payload, "iat": int(time.time()), "exp": int(time.time()) + expires_in}
        msg = f"{cls.b64encode(header)}.{cls.b64encode(payload)}"
        sig = hmac.new(secret.encode(), msg.encode(), hashlib.sha256).hexdigest()
        return f"{msg}.{sig}"

    @classmethod
    def verify_token(cls, token, secret):
        try:
            header_b64, payload_b64, sig = token.rsplit(".", 2)
            msg = f"{header_b64}.{payload_b64}"
            expected_sig = hmac.new(secret.encode(), msg.encode(), hashlib.sha256).hexdigest()
            if sig != expected_sig:
                raise ValueError("Invalid signature")
            payload = cls.b64decode(payload_b64)
            if payload.get("exp", 0) < int(time.time()):
                raise ValueError("Token expired")
            return payload
        except Exception as e:
            raise ValueError(f"Invalid token: {e}")

class JWTAuthSystem:
    SECRET = "django-super-secret-key-change-in-production"
    ACCESS_LIFETIME = 3600      # 1 hour
    REFRESH_LIFETIME = 7 * 86400  # 7 days

    users = {
        "alice": {"id": 1, "password": "secret123", "email": "alice@example.com", "is_staff": False},
        "admin": {"id": 2, "password": "admin123", "email": "admin@site.com", "is_staff": True},
    }

    @classmethod
    def obtain_token(cls, username, password):
        user = cls.users.get(username)
        if not user or user["password"] != password:
            return {"error": "Invalid credentials"}, 401

        payload = {
            "user_id": user["id"],
            "username": username,
            "email": user["email"],
            "is_staff": user["is_staff"],
        }
        access = JWT.create_token(payload, cls.SECRET, cls.ACCESS_LIFETIME)
        refresh = JWT.create_token({"user_id": user["id"], "type": "refresh"},
                                    cls.SECRET, cls.REFRESH_LIFETIME)
        return {"access": access, "refresh": refresh}, 200

    @classmethod
    def refresh_token(cls, refresh_token):
        try:
            payload = JWT.verify_token(refresh_token, cls.SECRET)
            if payload.get("type") != "refresh":
                return {"error": "Not a refresh token"}, 400
            user = next((u for u in cls.users.values() if u["id"] == payload["user_id"]), None)
            if not user:
                return {"error": "User not found"}, 404
            username = next(k for k, v in cls.users.items() if v["id"] == user["id"])
            new_access = JWT.create_token(
                {"user_id": user["id"], "username": username, "email": user["email"]},
                cls.SECRET, cls.ACCESS_LIFETIME
            )
            return {"access": new_access}, 200
        except ValueError as e:
            return {"error": str(e)}, 401

    @classmethod
    def authenticate_request(cls, token_header):
        if not token_header or not token_header.startswith("Bearer "):
            return None, "No token provided"
        token = token_header[7:]
        try:
            payload = JWT.verify_token(token, cls.SECRET)
            return payload, None
        except ValueError as e:
            return None, str(e)

print("=== JWT Token Flow ===")

# Step 1: Login
print("1. POST /api/token/ (login)")
resp, status = JWTAuthSystem.obtain_token("alice", "secret123")
print(f"   Status: {status}")
access_token = resp.get("access", "")
refresh_token = resp.get("refresh", "")
print(f"   Access token: {access_token[:40]}...")
print(f"   Refresh token: {refresh_token[:40]}...")

print()
# Step 2: Use token
print("2. GET /api/profile/ with Bearer token")
payload, error = JWTAuthSystem.authenticate_request(f"Bearer {access_token}")
if payload:
    print(f"   Authenticated as: {payload['username']} (staff={payload['is_staff']})")
else:
    print(f"   Error: {error}")

print()
# Step 3: Wrong token
print("3. GET /api/profile/ with invalid token")
payload, error = JWTAuthSystem.authenticate_request("Bearer invalid.token.here")
print(f"   Error: {error}")

print()
# Step 4: Refresh
print("4. POST /api/token/refresh/")
resp, status = JWTAuthSystem.refresh_token(refresh_token)
print(f"   Status: {status}")
print(f"   New access token: {resp.get('access','')[:40]}...")

print()
# Step 5: Admin login
print("5. Admin login test")
resp, status = JWTAuthSystem.obtain_token("admin", "admin123")
payload, _ = JWTAuthSystem.authenticate_request(f"Bearer {resp['access']}")
print(f"   Admin user: {payload['username']}, is_staff={payload['is_staff']}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 8: ADMIN PANEL
    # ================================================================
    {
        "title": "Django Admin",
        "slug": "django-admin",
        "description": "Customize the powerful built-in admin interface",
        "icon": "⚙️",
        "order": 8,
        "lessons": [
            {
                "title": "Admin Customization",
                "slug": "admin-customization",
                "difficulty": "intermediate",
                "order": 1,
                "content": '''# Django Admin Customization

Django's admin is a fully-featured interface generated from your models. It's one of Django's killer features.

## Basic Registration

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Tag

# Simple registration
admin.site.register(Post)

# With customization
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # List view columns
    list_display = ['title', 'author', 'category', 'is_published', 'views', 'created_at']

    # Filters sidebar
    list_filter = ['is_published', 'category', 'created_at', 'author']

    # Search box
    search_fields = ['title', 'content', 'author__username']

    # Click to edit (default is just the first field)
    list_display_links = ['title']

    # Editable in list view
    list_editable = ['is_published']

    # Ordering
    ordering = ['-created_at']

    # Number of items per page
    list_per_page = 20

    # Date drill-down navigation
    date_hierarchy = 'created_at'

    # Prepopulate slug from title
    prepopulated_fields = {'slug': ('title',)}

    # Read-only fields in form
    readonly_fields = ['created_at', 'updated_at', 'views']

    # Fields layout in form
    fields = ['title', 'slug', 'author', 'category', 'content', 'is_published']
    # OR use fieldsets for grouped layout:
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Settings', {
            'fields': ('is_published', 'featured'),
            'classes': ('collapse',)  # Collapsible section
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'views'),
            'classes': ('collapse',)
        }),
    )
```

## Custom List Display Methods

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status_badge', 'view_count', 'created_at']

    @admin.display(description='Status', ordering='is_published')
    def status_badge(self, obj):
        from django.utils.html import format_html
        if obj.is_published:
            return format_html('<span style="color:green;">● Published</span>')
        return format_html('<span style="color:orange;">● Draft</span>')

    @admin.display(description='Views', ordering='views')
    def view_count(self, obj):
        return f"{obj.views:,}"  # Format with commas
```

## Admin Actions

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['publish_posts', 'unpublish_posts', 'export_csv']

    @admin.action(description='Publish selected posts')
    def publish_posts(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'{count} post(s) published.')

    @admin.action(description='Unpublish selected posts')
    def unpublish_posts(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'{count} post(s) unpublished.', level='warning')

    @admin.action(description='Export to CSV')
    def export_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="posts.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Title', 'Author', 'Published', 'Views'])
        for post in queryset:
            writer.writerow([post.id, post.title, post.author, post.is_published, post.views])
        return response
```

## Inline Models

Edit related objects on the same page:

```python
class CommentInline(admin.TabularInline):  # or StackedInline
    model = Comment
    extra = 1            # Extra blank forms
    max_num = 10
    readonly_fields = ['created_at']
    fields = ['author', 'content', 'is_approved']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

## Custom Admin Site

```python
# admin.py
class MyAdminSite(admin.AdminSite):
    site_header = 'DjangoLearn Administration'
    site_title = 'DjangoLearn Admin'
    index_title = 'Welcome to DjangoLearn Admin'

my_admin = MyAdminSite(name='myadmin')

# urls.py
urlpatterns = [
    path('my-admin/', my_admin.urls),
]
```

## Admin Security Tips

```python
# Restrict access by IP (middleware)
class AdminIPRestrictionMiddleware:
    ALLOWED_IPS = ['127.0.0.1', '192.168.1.100']

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            if request.META.get('REMOTE_ADDR') not in self.ALLOWED_IPS:
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden()
        return self.get_response(request)
```

---

> 💡 Change your admin URL from `/admin/` to something obscure in production: `path('secret-panel-xyz/', admin.site.urls)`
''',
                "code_example": '''# Django Admin configuration simulation

class Model:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    def __repr__(self):
        return f"{self.__class__.__name__}({getattr(self,'title', getattr(self,'name', self.__class__.__name__))})"

class Post(Model): pass
class Comment(Model): pass

# Simulated QuerySet
class QuerySet:
    def __init__(self, items): self._items = items
    def filter(self, **kw): return QuerySet([i for i in self._items if all(getattr(i, k, None) == v for k,v in kw.items())])
    def update(self, **kw):
        count = 0
        for item in self._items:
            for k, v in kw.items():
                setattr(item, k, v)
            count += 1
        return count
    def __iter__(self): return iter(self._items)
    def __len__(self): return len(self._items)

# Admin registration system
class AdminRegistry:
    _registry = {}

    @classmethod
    def register(cls, model, admin_class=None):
        cls._registry[model.__name__] = {
            "model": model,
            "admin": admin_class or ModelAdmin,
        }

    @classmethod
    def get_admin(cls, model_name):
        return cls._registry.get(model_name)

class ModelAdmin:
    list_display = ["__str__"]
    list_filter = []
    search_fields = []
    list_per_page = 20
    ordering = []
    readonly_fields = []
    actions = []

    def __init__(self, model, queryset):
        self.model = model
        self.queryset = queryset

    def changelist_view(self, search=None, filters=None, page=1):
        items = list(self.queryset)
        if search and self.search_fields:
            items = [i for i in items if any(
                search.lower() in str(getattr(i, f, "")).lower()
                for f in self.search_fields
            )]
        if filters:
            for k, v in filters.items():
                items = [i for i in items if getattr(i, k, None) == v]
        start = (page - 1) * self.list_per_page
        page_items = items[start:start+self.list_per_page]
        return {
            "total": len(items),
            "page": page,
            "items": page_items,
            "columns": self.list_display,
        }

    def execute_action(self, action_name, queryset):
        method = getattr(self, action_name, None)
        if method:
            return method(queryset)
        return f"Action '{action_name}' not found"

class PostAdmin(ModelAdmin):
    list_display = ["title", "author", "is_published", "views"]
    list_filter = ["is_published", "author"]
    search_fields = ["title", "content"]
    list_per_page = 3
    ordering = ["-views"]
    actions = ["publish_posts", "unpublish_posts"]

    def publish_posts(self, queryset):
        count = queryset.update(is_published=True)
        return f"{count} post(s) published"

    def unpublish_posts(self, queryset):
        count = queryset.update(is_published=False)
        return f"{count} post(s) unpublished"

    def status_badge(self, obj):
        return "Published" if obj.is_published else "Draft"

# Sample data
posts = QuerySet([
    Post(id=1, title="Django Intro", author="alice", is_published=True, views=1500, content="Django is great"),
    Post(id=2, title="ORM Guide", author="alice", is_published=False, views=0, content="Querysets are lazy"),
    Post(id=3, title="REST APIs", author="bob", is_published=True, views=3200, content="DRF is awesome"),
    Post(id=4, title="Testing", author="bob", is_published=True, views=450, content="Test your code"),
    Post(id=5, title="Deployment", author="charlie", is_published=False, views=0, content="Deploy to Render"),
])

# Register
AdminRegistry.register(Post, PostAdmin)

# Use admin
admin = PostAdmin(Post, posts)

print("=== Django Admin: Post List ===")
view = admin.changelist_view()
print(f"Total posts: {view['total']}, Page {view['page']}")
print(f"Columns: {view['columns']}")
for item in view['items']:
    print(f"  [{item.id}] {item.title:20} | {item.author:8} | {'Published' if item.is_published else 'Draft':10} | {item.views} views")

print()
print("=== Search: 'django' ===")
view = admin.changelist_view(search="django")
for item in view['items']:
    print(f"  {item.title}")

print()
print("=== Filter: author=alice ===")
view = admin.changelist_view(filters={"author": "alice"})
for item in view['items']:
    print(f"  {item.title} (published={item.is_published})")

print()
print("=== Action: publish_posts ===")
drafts = posts.filter(is_published=False)
result = admin.execute_action("publish_posts", drafts)
print(f"Result: {result}")
view = admin.changelist_view(filters={"is_published": True})
print(f"Now published: {view['total']} posts")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 9: MIDDLEWARE & SIGNALS
    # ================================================================
    {
        "title": "Middleware & Signals",
        "slug": "middleware-signals",
        "description": "Hook into Django's request lifecycle with middleware and signals",
        "icon": "🔄",
        "order": 9,
        "lessons": [
            {
                "title": "Custom Middleware",
                "slug": "custom-middleware",
                "difficulty": "advanced",
                "order": 1,
                "content": '''# Custom Middleware

Middleware processes requests and responses globally before they reach views.

## How Middleware Works

```
Request → Middleware1 → Middleware2 → View → Middleware2 → Middleware1 → Response
```

## Writing Middleware

```python
# mysite/middleware.py

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time setup when server starts

    def __call__(self, request):
        # Code before the view runs
        print(f"Before view: {request.path}")

        response = self.get_response(request)

        # Code after the view runs
        print(f"After view: {response.status_code}")

        return response

    def process_exception(self, request, exception):
        # Called if view raises an exception
        print(f"Exception in {request.path}: {exception}")
        return None  # Return None to propagate exception
```

Register in `settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'mysite.middleware.SimpleMiddleware',  # ← Add yours
    ...
]
```

## Real-World Examples

### Request Timing Middleware
```python
import time

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start

        response['X-Response-Time'] = f"{duration:.3f}s"
        if duration > 1.0:
            print(f"SLOW: {request.path} took {duration:.2f}s")
        return response
```

### Maintenance Mode Middleware
```python
from django.http import HttpResponse
from django.conf import settings

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'MAINTENANCE_MODE', False):
            if not request.path.startswith('/admin/'):
                return HttpResponse(
                    "<h1>Under Maintenance</h1><p>Back soon!</p>",
                    status=503
                )
        return self.get_response(request)
```

### API Rate Limiting Middleware
```python
from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = 100  # requests
        self.window = 3600  # per hour

    def __call__(self, request):
        if request.path.startswith('/api/'):
            ip = request.META.get('REMOTE_ADDR')
            key = f"ratelimit:{ip}"
            count = cache.get(key, 0)
            if count >= self.limit:
                return JsonResponse(
                    {'error': 'Rate limit exceeded. Try again in 1 hour.'},
                    status=429
                )
            cache.set(key, count + 1, self.window)
        return self.get_response(request)
```

## Signals

Signals let decoupled apps get notified when actions happen elsewhere.

```python
# accounts/signals.py
from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

# Create profile after user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print(f"Profile created for {instance.email}")

# Send welcome email
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Welcome!',
            message=f'Hi {instance.username}, welcome to our site!',
            from_email='noreply@mysite.com',
            recipient_list=[instance.email],
        )

# Log logins
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print(f"User {user.email} logged in from {request.META.get('REMOTE_ADDR')}")

# Clean up on delete
@receiver(pre_delete, sender=User)
def cleanup_user_data(sender, instance, **kwargs):
    # Delete files before deleting user
    if instance.profile.avatar:
        instance.profile.avatar.delete(save=False)
```

```python
# accounts/apps.py
class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals  # ← Connect signals when app is ready
```

## Custom Signals

```python
from django.dispatch import Signal

# Define signal
post_published = Signal()

# Send signal
class Post(models.Model):
    def publish(self):
        self.is_published = True
        self.save()
        post_published.send(sender=self.__class__, post=self)

# Listen to signal
@receiver(post_published)
def on_post_published(sender, post, **kwargs):
    notify_subscribers(post)
    update_sitemap()
    ping_search_engines(post.get_absolute_url())
```

---

> 💡 Use **signals** for loose coupling — when app A needs to react to something in app B without directly importing from it.
''',
                "code_example": '''# Middleware and Signals simulation

import time
from collections import defaultdict

# ======= MIDDLEWARE SYSTEM =======
class Request:
    def __init__(self, method, path, ip="127.0.0.1"):
        self.method = method
        self.path = path
        self.META = {"REMOTE_ADDR": ip}
        self.user_id = None

class Response:
    def __init__(self, content, status=200):
        self.content = content
        self.status_code = status
        self.headers = {}
    def __repr__(self):
        return f"Response({self.status_code})"

def mock_view(request):
    time.sleep(0.001)  # Simulate work
    return Response(f"<html>Content for {request.path}</html>")

class MiddlewareStack:
    def __init__(self, view):
        self.view = view
        self.middlewares = []
        self.logs = []

    def add(self, middleware_class):
        self.middlewares.insert(0, middleware_class)

    def process(self, request):
        # Build the middleware chain
        handler = self.view
        for mw_class in reversed(self.middlewares):
            handler = mw_class(handler, self.logs)
        return handler(request)

class TimingMiddleware:
    def __init__(self, get_response, logs):
        self.get_response = get_response
        self.logs = logs

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = (time.time() - start) * 1000
        response.headers["X-Response-Time"] = f"{duration:.2f}ms"
        self.logs.append(f"[Timing] {request.path}: {duration:.2f}ms")
        return response

class RateLimitMiddleware:
    _counts = defaultdict(int)
    LIMIT = 3  # Per IP per "session"

    def __init__(self, get_response, logs):
        self.get_response = get_response
        self.logs = logs

    def __call__(self, request):
        ip = request.META["REMOTE_ADDR"]
        self._counts[ip] += 1
        self.logs.append(f"[RateLimit] {ip}: {self._counts[ip]}/{self.LIMIT} requests")
        if self._counts[ip] > self.LIMIT:
            return Response('{"error": "Rate limit exceeded"}', status=429)
        return self.get_response(request)

class LoggingMiddleware:
    def __init__(self, get_response, logs):
        self.get_response = get_response
        self.logs = logs

    def __call__(self, request):
        self.logs.append(f"[Log] --> {request.method} {request.path}")
        response = self.get_response(request)
        self.logs.append(f"[Log] <-- {response.status_code}")
        return response

# Build stack
stack = MiddlewareStack(mock_view)
stack.add(LoggingMiddleware)
stack.add(TimingMiddleware)
stack.add(RateLimitMiddleware)

print("=== Middleware Stack (3 requests) ===")
for path in ["/blog/", "/api/posts/", "/api/users/"]:
    resp = stack.process(Request("GET", path))
    print(f"  {path} -> {resp}")
print()

print("=== Rate Limiting (same IP, 4 requests) ===")
stack2 = MiddlewareStack(mock_view)
stack2.add(RateLimitMiddleware)
for i in range(4):
    resp = stack2.process(Request("GET", "/api/data/", ip="1.2.3.4"))
    print(f"  Request {i+1}: {resp}")

print()
print("=== Middleware Logs ===")
for log in stack.logs[-6:]:
    print(f"  {log}")

# ======= SIGNALS SYSTEM =======
print()
print("=== Signal System ===")

class Signal:
    def __init__(self):
        self.receivers = []

    def connect(self, receiver, sender=None):
        self.receivers.append((receiver, sender))

    def send(self, sender, **kwargs):
        responses = []
        for receiver, filter_sender in self.receivers:
            if filter_sender is None or filter_sender == sender:
                result = receiver(sender=sender, **kwargs)
                responses.append((receiver.__name__, result))
        return responses

# Define signals
post_save = Signal()
post_delete = Signal()
user_logged_in = Signal()

# Define receivers
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(f"  [Signal] Profile created for {instance['email']}")
        return "profile_created"

def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"  [Signal] Welcome email sent to {instance['email']}")
        return "email_sent"

def log_login(sender, user, **kwargs):
    print(f"  [Signal] User {user['email']} logged in")
    return "login_logged"

# Connect signals
post_save.connect(create_profile)
post_save.connect(send_welcome_email)
user_logged_in.connect(log_login)

# Trigger signals
print("Creating user...")
user = {"id": 1, "email": "alice@example.com", "username": "alice"}
post_save.send(sender="User", instance=user, created=True)

print()
print("User login...")
user_logged_in.send(sender="Auth", user=user)
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 10: TESTING
    # ================================================================
    {
        "title": "Testing Django Apps",
        "slug": "testing",
        "description": "Write unit tests, integration tests, and API tests",
        "icon": "🧪",
        "order": 10,
        "lessons": [
            {
                "title": "Writing Tests",
                "slug": "writing-tests",
                "difficulty": "intermediate",
                "order": 1,
                "content": '''# Writing Tests in Django

Django has a built-in test framework based on Python's `unittest`. Good tests prevent regressions and document expected behavior.

## Test Structure

```python
# blog/tests.py
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, Category

User = get_user_model()

class PostModelTest(TestCase):
    """Test the Post model"""

    @classmethod
    def setUpTestData(cls):
        """Set up data once for all tests in this class"""
        cls.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        cls.category = Category.objects.create(
            name='Python', slug='python'
        )
        cls.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=cls.user,
            category=cls.category,
            is_published=True,
        )

    def test_post_creation(self):
        """Post should be created with correct attributes"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertTrue(self.post.is_published)

    def test_post_str(self):
        """Post __str__ should return title"""
        self.assertEqual(str(self.post), 'Test Post')

    def test_post_views_default(self):
        """Views should default to 0"""
        self.assertEqual(self.post.views, 0)

    def test_slug_auto_generated(self):
        """Slug should be auto-generated from title"""
        self.assertEqual(self.post.slug, 'test-post')
```

## View Tests

```python
class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('user', 'u@test.com', 'pass123')
        self.post = Post.objects.create(
            title='Test', content='Content', author=self.user, is_published=True
        )

    def test_post_list_view(self):
        """List view should return 200 and contain post"""
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        """Detail view should return 200 for published post"""
        url = reverse('blog:detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

    def test_post_detail_404(self):
        """Detail view should return 404 for non-existent post"""
        response = self.client.get(reverse('blog:detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

    def test_create_post_requires_login(self):
        """Create view should redirect unauthenticated users"""
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertIn('/accounts/login/', response.url)

    def test_create_post_authenticated(self):
        """Authenticated user can create a post"""
        self.client.login(username='user', password='pass123')
        response = self.client.post(reverse('blog:create'), {
            'title': 'New Post',
            'content': 'New content here.',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Post.objects.filter(title='New Post').exists())
```

## API Tests (DRF)

```python
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('api_user', 'api@test.com', 'pass')
        self.client = APIClient()
        self.post = Post.objects.create(
            title='API Test Post', content='Content', author=self.user, is_published=True
        )

    def test_list_posts_unauthenticated(self):
        """Anyone can list posts"""
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_post_authenticated(self):
        """Authenticated user can create via API"""
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New API Post', 'content': 'API Content'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New API Post')

    def test_create_post_unauthenticated(self):
        """Unauthenticated user cannot create"""
        response = self.client.post('/api/posts/', {'title': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

## Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app
python manage.py test blog

# Run specific class
python manage.py test blog.tests.PostModelTest

# Run specific test
python manage.py test blog.tests.PostModelTest.test_post_creation

# With verbosity
python manage.py test --verbosity=2

# Coverage report
pip install coverage
coverage run manage.py test
coverage report
coverage html  # HTML report in htmlcov/
```

## Test Assertions Reference

```python
# Status codes
self.assertEqual(response.status_code, 200)

# Content
self.assertContains(response, 'text')
self.assertNotContains(response, 'text')

# Templates
self.assertTemplateUsed(response, 'template.html')

# Redirects
self.assertRedirects(response, '/expected/url/')

# Database
self.assertTrue(Post.objects.filter(title='Test').exists())
self.assertEqual(Post.objects.count(), 5)

# General assertions
self.assertEqual(a, b)
self.assertNotEqual(a, b)
self.assertTrue(condition)
self.assertFalse(condition)
self.assertIsNone(value)
self.assertIn(item, collection)
self.assertRaises(Exception, callable)
```

---

> 💡 Aim for **70%+ test coverage**. Focus on testing your business logic and edge cases, not Django's built-in functionality.
''',
                "code_example": '''# Django test framework simulation

import traceback
from collections import defaultdict

class TestResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.errors = []

    def add_success(self, name):
        self.passed.append(name)

    def add_failure(self, name, msg):
        self.failed.append((name, msg))

    def add_error(self, name, exc):
        self.errors.append((name, str(exc)))

    def summary(self):
        total = len(self.passed) + len(self.failed) + len(self.errors)
        return {
            "total": total,
            "passed": len(self.passed),
            "failed": len(self.failed),
            "errors": len(self.errors),
            "ok": len(self.failed) == 0 and len(self.errors) == 0,
        }

class TestCase:
    def assertEqual(self, a, b, msg=None):
        if a != b:
            raise AssertionError(msg or f"{repr(a)} != {repr(b)}")

    def assertNotEqual(self, a, b, msg=None):
        if a == b:
            raise AssertionError(msg or f"{repr(a)} == {repr(b)}")

    def assertTrue(self, val, msg=None):
        if not val:
            raise AssertionError(msg or f"Expected True, got {repr(val)}")

    def assertFalse(self, val, msg=None):
        if val:
            raise AssertionError(msg or f"Expected False, got {repr(val)}")

    def assertIn(self, item, container, msg=None):
        if item not in container:
            raise AssertionError(msg or f"{repr(item)} not in {repr(container)}")

    def assertRaises(self, exception, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            raise AssertionError(f"Expected {exception.__name__} was not raised")
        except exception:
            pass

# Our "models"
class Post:
    _db = {}
    _counter = 0

    def __init__(self, **kwargs):
        Post._counter += 1
        self.id = Post._counter
        self.title = kwargs.get("title", "")
        self.content = kwargs.get("content", "")
        self.views = kwargs.get("views", 0)
        self.is_published = kwargs.get("is_published", False)
        self.author = kwargs.get("author", "")
        Post._db[self.id] = self

    def __str__(self):
        return self.title

    def save(self):
        Post._db[self.id] = self

    @classmethod
    def objects_create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def objects_get(cls, **kwargs):
        for post in cls._db.values():
            if all(getattr(post, k, None) == v for k, v in kwargs.items()):
                return post
        raise Exception("DoesNotExist")

    @classmethod
    def objects_filter(cls, **kwargs):
        return [p for p in cls._db.values()
                if all(getattr(p, k, None) == v for k, v in kwargs.items())]

    @classmethod
    def objects_count(cls):
        return len(cls._db)

    @classmethod
    def reset(cls):
        cls._db = {}
        cls._counter = 0

# Test classes
class PostModelTests(TestCase):
    def setUp(self):
        Post.reset()
        self.post = Post.objects_create(
            title="Test Post", content="Test content here.",
            author="alice", is_published=True
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author, "alice")
        self.assertTrue(self.post.is_published)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_views_default_zero(self):
        self.assertEqual(self.post.views, 0)

    def test_views_increment(self):
        self.post.views += 1
        self.post.save()
        updated = Post.objects_get(id=self.post.id)
        self.assertEqual(updated.views, 1)

    def test_filter_published(self):
        Post.objects_create(title="Draft", content="...", author="bob", is_published=False)
        published = Post.objects_filter(is_published=True)
        self.assertEqual(len(published), 1)
        self.assertEqual(published[0].title, "Test Post")

    def test_post_does_not_exist(self):
        self.assertRaises(Exception, Post.objects_get, id=999)

class PostValidationTests(TestCase):
    def test_empty_title_fails(self):
        post = Post.objects_create(title="", content="content", author="alice")
        self.assertFalse(bool(post.title))

    def test_long_title(self):
        long_title = "A" * 201
        post = Post.objects_create(title=long_title, content="content", author="alice")
        self.assertTrue(len(post.title) > 200)

def run_tests(*test_classes):
    result = TestResult()
    for cls in test_classes:
        instance = cls()
        test_methods = [m for m in dir(cls) if m.startswith("test_")]
        for method_name in test_methods:
            full_name = f"{cls.__name__}.{method_name}"
            try:
                if hasattr(instance, "setUp"):
                    instance.setUp()
                getattr(instance, method_name)()
                result.add_success(full_name)
            except AssertionError as e:
                result.add_failure(full_name, str(e))
            except Exception as e:
                result.add_error(full_name, e)
    return result

print("Running Django Tests...")
print("=" * 45)
result = run_tests(PostModelTests, PostValidationTests)

for name in result.passed:
    print(f"  PASS  {name}")
for name, msg in result.failed:
    print(f"  FAIL  {name}: {msg}")
for name, err in result.errors:
    print(f"  ERROR {name}: {err}")

print()
summary = result.summary()
status = "OK" if summary["ok"] else "FAILED"
print(f"{'='*45}")
print(f"Ran {summary['total']} tests | {status}")
print(f"  Passed: {summary['passed']} | Failed: {summary['failed']} | Errors: {summary['errors']}")
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 11: DEPLOYMENT
    # ================================================================
    {
        "title": "Deployment",
        "slug": "deployment",
        "description": "Deploy Django apps to production for free",
        "icon": "🌐",
        "order": 11,
        "lessons": [
            {
                "title": "Deploying to Production",
                "slug": "production-deployment",
                "difficulty": "advanced",
                "order": 1,
                "content": '''# Deploying Django to Production

## Pre-Deployment Checklist

```bash
python manage.py check --deploy
```

### Security Settings

```python
# settings.py (production)
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Security headers
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

## Deploying to Render.com (Free)

### Step 1: `render.yaml`
```yaml
services:
  - type: web
    name: my-django-app
    env: python
    buildCommand: >
      pip install -r requirements.txt &&
      python manage.py migrate &&
      python manage.py collectstatic --no-input
    startCommand: gunicorn mysite.wsgi:application
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: "False"
      - key: DATABASE_URL
        fromDatabase:
          name: mydb
          property: connectionString

databases:
  - name: mydb
    plan: free
```

### Step 2: `requirements.txt`
```
django==4.2.7
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
dj-database-url==2.1.0
```

### Step 3: Production settings
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Static files with Whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Right after security
    ...
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Deploying to Railway.app (Free Tier)

```bash
# Install Railway CLI
npm install -g @railway/cli

railway login
railway init
railway up
```

Set environment variables in Railway dashboard:
- `SECRET_KEY`
- `DEBUG=False`
- `DATABASE_URL` (auto-provided)

## Environment Variables

Never hardcode secrets! Use a `.env` file locally:

```bash
# .env (don't commit this!)
SECRET_KEY=django-super-secret-xyz
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_PASSWORD=your-email-app-password
```

```python
# settings.py
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
```

## Static Files in Production

```python
# Install whitenoise
pip install whitenoise

# settings.py
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## Docker (Optional)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --no-input

EXPOSE 8000
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/mydb
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_PASSWORD: postgres
```

## Performance

```python
# Caching with Redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
    }
}

# Cache a view for 15 minutes
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def post_list(request):
    ...

# Low-level cache
from django.core.cache import cache
data = cache.get('my_key')
if data is None:
    data = expensive_query()
    cache.set('my_key', data, timeout=3600)
```

---

> 💡 **Free hosting options:**
> - Backend: [Render.com](https://render.com), [Railway.app](https://railway.app), [Fly.io](https://fly.io)
> - Frontend: [Vercel](https://vercel.com), [Netlify](https://netlify.com)
> - Database: Render PostgreSQL (free), Supabase (free tier)
''',
                "code_example": '''# Django deployment configuration checker

import os

class DeploymentChecker:
    def __init__(self, settings):
        self.settings = settings
        self.errors = []
        self.warnings = []
        self.ok = []

    def check_all(self):
        self._check_debug()
        self._check_secret_key()
        self._check_allowed_hosts()
        self._check_database()
        self._check_static_files()
        self._check_security()
        self._check_email()
        return self

    def _check_debug(self):
        if self.settings.get("DEBUG"):
            self.errors.append("DEBUG=True in production!")
        else:
            self.ok.append("DEBUG=False")

    def _check_secret_key(self):
        key = self.settings.get("SECRET_KEY", "")
        if "insecure" in key or "django-insecure" in key or len(key) < 40:
            self.errors.append("SECRET_KEY is weak or default!")
        else:
            self.ok.append("SECRET_KEY is strong")

    def _check_allowed_hosts(self):
        hosts = self.settings.get("ALLOWED_HOSTS", [])
        if "*" in hosts:
            self.errors.append("ALLOWED_HOSTS=['*'] — too permissive!")
        elif not hosts:
            self.errors.append("ALLOWED_HOSTS is empty!")
        else:
            self.ok.append(f"ALLOWED_HOSTS={hosts}")

    def _check_database(self):
        db = self.settings.get("DATABASE", {})
        engine = db.get("ENGINE", "")
        if "sqlite" in engine:
            self.warnings.append("Using SQLite in production (consider PostgreSQL)")
        elif "postgresql" in engine:
            self.ok.append("Using PostgreSQL")

    def _check_static_files(self):
        if not self.settings.get("STATIC_ROOT"):
            self.errors.append("STATIC_ROOT not configured!")
        else:
            self.ok.append("STATIC_ROOT configured")

        if not self.settings.get("WHITENOISE"):
            self.warnings.append("WhiteNoise not configured (needed for static files)")
        else:
            self.ok.append("WhiteNoise configured")

    def _check_security(self):
        security_settings = [
            ("SECURE_SSL_REDIRECT", True, "SSL redirect"),
            ("CSRF_COOKIE_SECURE", True, "Secure CSRF cookie"),
            ("SESSION_COOKIE_SECURE", True, "Secure session cookie"),
        ]
        for key, expected, label in security_settings:
            if self.settings.get(key) == expected:
                self.ok.append(f"{label} enabled")
            else:
                self.warnings.append(f"{label} not enabled (set {key}=True)")

    def _check_email(self):
        backend = self.settings.get("EMAIL_BACKEND", "")
        if "console" in backend:
            self.warnings.append("Email backend is 'console' — emails won't send!")
        elif "smtp" in backend:
            self.ok.append("SMTP email configured")

    def report(self):
        total = len(self.errors) + len(self.warnings) + len(self.ok)
        score = round((len(self.ok) / total) * 100) if total > 0 else 0
        print(f"Deployment Readiness Score: {score}%")
        print("=" * 40)

        if self.errors:
            print(f"ERRORS ({len(self.errors)}) — MUST FIX:")
            for e in self.errors:
                print(f"  ❌ {e}")

        if self.warnings:
            print(f"WARNINGS ({len(self.warnings)}) — Should fix:")
            for w in self.warnings:
                print(f"  ⚠️  {w}")

        if self.ok:
            print(f"OK ({len(self.ok)}):")
            for o in self.ok:
                print(f"  ✅ {o}")

        verdict = "NOT READY" if self.errors else ("READY WITH WARNINGS" if self.warnings else "READY TO DEPLOY")
        print(f"Verdict: {verdict}")

print("=== Development Settings ===")
dev_settings = {
    "DEBUG": True,
    "SECRET_KEY": "django-insecure-abc123",
    "ALLOWED_HOSTS": ["*"],
    "DATABASE": {"ENGINE": "django.db.backends.sqlite3"},
    "EMAIL_BACKEND": "django.core.mail.backends.console.EmailBackend",
    "STATIC_ROOT": None,
    "WHITENOISE": False,
    "SECURE_SSL_REDIRECT": False,
    "CSRF_COOKIE_SECURE": False,
    "SESSION_COOKIE_SECURE": False,
}
DeploymentChecker(dev_settings).check_all().report()

print()
print("=== Production Settings ===")
prod_settings = {
    "DEBUG": False,
    "SECRET_KEY": "prod-a7x9k2m4p8q1w5y3n6v0r4t8s2u7j9e1d",
    "ALLOWED_HOSTS": ["mysite.com", "www.mysite.com"],
    "DATABASE": {"ENGINE": "django.db.backends.postgresql", "HOST": "db.render.com"},
    "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
    "STATIC_ROOT": "/app/staticfiles",
    "WHITENOISE": True,
    "SECURE_SSL_REDIRECT": True,
    "CSRF_COOKIE_SECURE": True,
    "SESSION_COOKIE_SECURE": True,
}
DeploymentChecker(prod_settings).check_all().report()
'''
            },
        ]
    },

    # ================================================================
    # TOPIC 12: ADVANCED TOPICS
    # ================================================================
    {
        "title": "Advanced Django",
        "slug": "advanced-django",
        "description": "Caching, Celery, Channels, and production patterns",
        "icon": "🏆",
        "order": 12,
        "lessons": [
            {
                "title": "Caching Strategies",
                "slug": "caching-strategies",
                "difficulty": "advanced",
                "order": 1,
                "content": '''# Caching in Django

Caching dramatically improves performance by storing expensive computations.

## Cache Backends

```python
# settings.py

# In-memory (development)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# File-based
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Redis (production - recommended)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

## Levels of Caching

### Per-view caching
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutes
def post_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'blog/list.html', {'posts': posts})

# In URLs
urlpatterns = [
    path('', cache_page(60 * 15)(PostListView.as_view())),
]
```

### Template fragment caching
```html
{% load cache %}

{% cache 3600 sidebar %}
    {# Expensive sidebar content #}
    {% for post in popular_posts %}
        <a href="{{ post.url }}">{{ post.title }}</a>
    {% endfor %}
{% endcache %}

{# Cache with dynamic key #}
{% cache 3600 user_posts request.user.id %}
    {{ user.posts.count }} posts
{% endcache %}
```

### Low-level caching (most flexible)
```python
from django.core.cache import cache

# Simple get/set
cache.set('my_key', 'my_value', timeout=3600)
value = cache.get('my_key')

# Get or set
value = cache.get_or_set('my_key', expensive_function, 3600)

# Delete
cache.delete('my_key')

# Multiple keys
cache.set_many({'key1': 'val1', 'key2': 'val2'}, timeout=3600)
values = cache.get_many(['key1', 'key2'])

# Increment/decrement (atomic)
cache.set('page_views', 0)
cache.incr('page_views')
cache.decr('page_views')
```

### Cache in views (cache-aside pattern)
```python
def post_detail(request, pk):
    cache_key = f'post:{pk}'
    post = cache.get(cache_key)

    if post is None:
        post = get_object_or_404(Post, pk=pk)
        cache.set(cache_key, post, timeout=3600)

    return render(request, 'blog/detail.html', {'post': post})

# Invalidate on save (using signals)
from django.db.models.signals import post_save

@receiver(post_save, sender=Post)
def invalidate_post_cache(sender, instance, **kwargs):
    cache.delete(f'post:{instance.pk}')
```

## Celery: Background Tasks

```bash
pip install celery redis
```

```python
# celery.py
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

```python
# blog/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(user_id, post_id):
    """Run in background — doesn't block the request"""
    user = User.objects.get(id=user_id)
    post = Post.objects.get(id=post_id)
    send_mail(
        subject=f'New post: {post.title}',
        message=f'Check out this post: {post.get_absolute_url()}',
        from_email='noreply@mysite.com',
        recipient_list=[user.email],
    )

@shared_task
def generate_sitemap():
    """Scheduled task — run every hour"""
    posts = Post.objects.filter(is_published=True)
    # Generate sitemap...

# In views — fire and forget
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.is_published = True
    post.save()
    # Don't wait for email — run in background
    send_notification_email.delay(request.user.id, post.id)
    return redirect('blog:detail', pk=pk)
```

```bash
# Start Celery worker
celery -A mysite worker -l info

# Start Celery beat (scheduler)
celery -A mysite beat -l info
```

---

> 💡 Cache invalidation is one of the hardest problems in CS. A good rule: cache aggressively, invalidate on write.
''',
                "code_example": '''# Caching system simulation
import time
from collections import OrderedDict

class Cache:
    """LRU Cache with TTL (simulating Redis/Memcached)"""

    def __init__(self, max_size=100):
        self._store = OrderedDict()
        self._expires = {}
        self._hits = 0
        self._misses = 0
        self.max_size = max_size

    def set(self, key, value, timeout=300):
        if len(self._store) >= self.max_size and key not in self._store:
            self._store.popitem(last=False)  # Remove oldest
        self._store[key] = value
        self._store.move_to_end(key)
        self._expires[key] = time.time() + timeout

    def get(self, key, default=None):
        if key in self._store:
            if time.time() < self._expires.get(key, 0):
                self._store.move_to_end(key)
                self._hits += 1
                return self._store[key]
            else:
                self.delete(key)  # Expired
        self._misses += 1
        return default

    def delete(self, key):
        self._store.pop(key, None)
        self._expires.pop(key, None)

    def get_or_set(self, key, func, timeout=300):
        val = self.get(key)
        if val is None:
            val = func()
            self.set(key, val, timeout)
        return val

    def incr(self, key, delta=1):
        val = self.get(key, 0)
        self.set(key, val + delta)
        return val + delta

    def stats(self):
        total = self._hits + self._misses
        rate = (self._hits / total * 100) if total > 0 else 0
        return {"keys": len(self._store), "hits": self._hits,
                "misses": self._misses, "hit_rate": f"{rate:.1f}%"}

cache = Cache()

# Simulate database (slow)
db_calls = 0
def fetch_post_from_db(pk):
    global db_calls
    db_calls += 1
    time.sleep(0.001)  # Simulate slow DB
    return {"id": pk, "title": f"Post {pk}", "views": pk * 100}

def fetch_popular_posts():
    global db_calls
    db_calls += 1
    time.sleep(0.002)
    return [{"id": i, "title": f"Popular Post {i}"} for i in range(1, 6)]

# Cache-aside pattern
def get_post(pk):
    key = f"post:{pk}"
    post = cache.get(key)
    if post is None:
        post = fetch_post_from_db(pk)
        cache.set(key, post, timeout=3600)
    return post

# Test caching
print("=== Cache Performance Test ===")
print("First access (cache MISS — hits database):")
start = time.time()
for pk in [1, 2, 3, 4, 5]:
    post = get_post(pk)
    print(f"  Post {pk}: '{post['title']}' (DB calls: {db_calls})")

print()
db_before = db_calls
print("Second access (cache HIT — no database):")
start2 = time.time()
for pk in [1, 2, 3, 4, 5]:
    post = get_post(pk)
    print(f"  Post {pk}: '{post['title']}' (DB calls: {db_calls})")
print(f"  Extra DB calls: {db_calls - db_before} (should be 0!)")

print()
print("=== get_or_set ===")
popular = cache.get_or_set("popular_posts", fetch_popular_posts, timeout=1800)
print(f"Popular posts: {len(popular)} items")

popular2 = cache.get_or_set("popular_posts", fetch_popular_posts, timeout=1800)
print(f"Second fetch: {len(popular2)} items (from cache)")

print()
print("=== Counter (like page views) ===")
for _ in range(5):
    cache.incr("total_views")
print(f"Total views: {cache.get('total_views')}")

print()
print("=== Cache Stats ===")
stats = cache.stats()
for k, v in stats.items():
    print(f"  {k}: {v}")
print(f"  Total DB calls: {db_calls}")
'''
            },
            {
                "title": "Django Channels - WebSockets",
                "slug": "django-channels",
                "difficulty": "advanced",
                "order": 2,
                "content": '''# Django Channels — Real-time with WebSockets

Django Channels extends Django to handle WebSockets, chat, and real-time features.

## Installation

```bash
pip install channels channels-redis
```

```python
# settings.py
INSTALLED_APPS = ['channels']

ASGI_APPLICATION = 'mysite.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}
```

## ASGI Configuration

```python
# mysite/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
```

## WebSocket Consumer

```python
# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print(f"WebSocket connected: {self.room_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = self.scope['user'].username

        # Broadcast to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))
```

## Routing

```python
# chat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```

## Frontend JavaScript

```html
<!-- chat/templates/chat/room.html -->
<script>
const roomName = "{{ room_name }}";
const socket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${roomName}/`
);

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    addMessage(data.username, data.message);
};

socket.onclose = function(e) {
    console.error('WebSocket closed:', e);
};

function sendMessage(message) {
    socket.send(JSON.stringify({ message: message }));
}
</script>
```

## Sending from Django Views (to WebSocket)

```python
# From a regular Django view or Celery task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def notify_chat_room(room_name, message, username):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"chat_{room_name}",
        {
            "type": "chat_message",
            "message": message,
            "username": username,
        }
    )
```

## Use Cases for Channels

| Use Case | Example |
|----------|---------|
| **Chat** | Real-time messaging |
| **Notifications** | Live alerts |
| **Dashboard** | Real-time analytics |
| **Collaboration** | Google Docs-style editing |
| **Gaming** | Multiplayer games |
| **Trading** | Live stock prices |

---

> 💡 Use Channels for features that require **push** from server to client. For simple polling, a regular AJAX endpoint may be simpler.
''',
                "code_example": '''# WebSocket and Channel Layer simulation

import json
from collections import defaultdict
from datetime import datetime

class ChannelLayer:
    """Simulates Django Channels channel layer (like Redis)"""
    _groups = defaultdict(set)
    _messages = defaultdict(list)

    @classmethod
    def group_add(cls, group_name, channel_name):
        cls._groups[group_name].add(channel_name)
        print(f"  [ChannelLayer] {channel_name} joined group '{group_name}'")

    @classmethod
    def group_discard(cls, group_name, channel_name):
        cls._groups[group_name].discard(channel_name)
        print(f"  [ChannelLayer] {channel_name} left group '{group_name}'")

    @classmethod
    def group_send(cls, group_name, message):
        channels = cls._groups.get(group_name, set())
        for channel in channels:
            cls._messages[channel].append(message)

    @classmethod
    def receive_messages(cls, channel_name):
        msgs = cls._messages.pop(channel_name, [])
        return msgs

    @classmethod
    def group_members(cls, group_name):
        return len(cls._groups.get(group_name, set()))

channel_layer = ChannelLayer()

class WebSocketConsumer:
    """Simulates Django Channels consumer"""
    def __init__(self, user, room):
        self.user = user
        self.room = room
        self.channel_name = f"channel_{user}_{id(self)}"
        self.group_name = f"chat_{room}"
        self.connected = False
        self.received = []

    def connect(self):
        channel_layer.group_add(self.group_name, self.channel_name)
        self.connected = True
        return {"type": "websocket.connect", "accepted": True}

    def disconnect(self):
        channel_layer.group_discard(self.group_name, self.channel_name)
        self.connected = False

    def send_message(self, message):
        """Client sends a message"""
        channel_layer.group_send(self.group_name, {
            "type": "chat_message",
            "message": message,
            "username": self.user,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
        })

    def tick(self):
        """Process incoming messages (simulates event loop)"""
        msgs = channel_layer.receive_messages(self.channel_name)
        for msg in msgs:
            if msg["type"] == "chat_message":
                self.received.append(msg)
        return msgs

    def __repr__(self):
        return f"Consumer({self.user}@{self.room})"

# Simulate a chat room
print("=== Django Channels: Chat Room Simulation ===")
print()

# Users connect
print("Connecting users to 'general' room...")
alice = WebSocketConsumer("alice", "general")
bob = WebSocketConsumer("bob", "general")
charlie = WebSocketConsumer("charlie", "general")

alice.connect()
bob.connect()
charlie.connect()

print(f"Room 'general' members: {channel_layer.group_members('chat_general')}")
print()

# Send messages
print("=== Sending Messages ===")
alice.send_message("Hey everyone! Welcome to DjangoLearn chat!")
bob.send_message("Hi Alice! Love the Django tutorials!")
charlie.send_message("Can someone explain WebSockets?")

# Process messages (all receive all messages)
print()
print("=== Messages Received ===")
for consumer in [alice, bob, charlie]:
    msgs = consumer.tick()
    print(f"{consumer.user} received {len(msgs)} message(s):")
    for msg in msgs:
        print(f"  [{msg['timestamp']}] {msg['username']}: {msg['message']}")
    print()

# Someone disconnects
print("=== Charlie Disconnects ===")
charlie.disconnect()
print(f"Room 'general' members: {channel_layer.group_members('chat_general')}")

# Message after disconnect
alice.send_message("Is Charlie still here?")
alice.tick()
bob.tick()
charlie_msgs = charlie.tick()
print(f"Charlie receives after disconnect: {len(charlie_msgs)} message(s) (should be 0)")

# Notification from server
print()
print("=== Server Push Notification ===")
def notify_room(room, message, from_user="system"):
    channel_layer.group_send(f"chat_{room}", {
        "type": "chat_message",
        "message": message,
        "username": from_user,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
    })

notify_room("general", "New lesson published: Advanced Django!", "DjangoLearn Bot")
for consumer in [alice, bob]:
    msgs = consumer.tick()
    for msg in msgs:
        print(f"  {consumer.user} got: [{msg['username']}] {msg['message']}")
'''
            },
        ]
    },
]


class Command(BaseCommand):
    help = 'Seed complete A-Z Django tutorial content'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding A-Z Django content...'))
        total_topics = 0
        total_lessons = 0

        for topic_data in TOPICS:
            lessons_data = topic_data.pop('lessons')
            topic, created = Topic.objects.update_or_create(
                slug=topic_data['slug'],
                defaults=topic_data
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status} topic: {topic.icon} {topic.title}')
            total_topics += 1

            for lesson_data in lessons_data:
                lesson, created = Lesson.objects.update_or_create(
                    topic=topic,
                    slug=lesson_data['slug'],
                    defaults=lesson_data
                )
                ls = 'Created' if created else 'Updated'
                self.stdout.write(f'    {ls} lesson: {lesson.title} [{lesson.difficulty}]')
                total_lessons += 1

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Done! {total_topics} topics, {total_lessons} lessons seeded.'
        ))

