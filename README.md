# Django REST API E-commerce System

An advanced and feature-rich E-commerce API developed with Django REST Framework. This API supports user authentication, product management, wishlist functionality, and role-based access control (Superuser, Staff, and Regular Users).

---

## Features

### Authentication
- User Registration
- Login and Logout
- Password Reset
- View & Update Profile
- Role-based Access Control (Superuser, Staff, Regular Users)

### Product Management
- View All Products
- Create, Update, and Delete Products (Staff Only)
- Search and Filter Products by Category
- Add and View Product Reviews

### Wishlist
- Add Products to Wishlist
- View Wishlist Items
- Remove Products from Wishlist

---

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), PostgreSQL (recommended for production)
- **Authentication:** Token-Based Authentication (DRF Simple JWT)

---




## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/robiulsunnyemon/ecommerce_project_api.git
cd ecommerce_project_api

```
### 2. Set Up Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```
### 4. Configure the Database
- Update the DATABASES setting in settings.py to match your database credentials.

- Default configuration (SQLite):
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
              }
        }

```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate

```
### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
- Open your browser and navigate to http://127.0.0.1:8000/.