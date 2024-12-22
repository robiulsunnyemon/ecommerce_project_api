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

---
## API Endpoints

- Authentication Endpoints
---

| Name                   | Endpoint                    | Method | Permission        | Description                                    |
|------------------------|-----------------------------|--------|-------------------|------------------------------------------------|
| User Registration       | /users/register/            | POST   | Public            | Register a new user.                          |
| User Login              | /users/login/               | POST   | Public            | Login and receive an authentication token.    |
| User Logout             | /users/logout/              | POST   | Logged-in Users   | Logout and invalidate the token.              |
| View Profile            | /users/profile/             | GET    | Logged-in Users   | View the logged-in user's profile.            |
| Update Password         | /users/update-password/     | PUT    | Logged-in Users   | Change the user's password.                   |
| Reset Password          | /users/reset-password/      | POST   | Public            | Send a password reset link to the email.      |
| List Users              | /users/                     | GET    | Superuser Only    | View all registered users.                    |
| List Staff Users        | /users/staff-users/         | GET    | Staff Only        | View a list of all staff users.               |
| List Superusers         | /users/super-users/         | GET    | Superuser Only    | View a list of all superusers.                |


- Product Endpoints
---

| Name            | Endpoint                        | Method | Permission        | Description                                      |
|-----------------|---------------------------------|--------|-------------------|--------------------------------------------------|
| List Products   | /products/                      | GET    | Public            | View all products.                              |
| Create Product  | /products/                      | POST   | Staff Only        | Create a new product.                           |
| Update Product  | /products/<id>/                 | PUT    | Staff Only        | Update a product.                               |
| Delete Product  | /products/<id>/                 | DELETE | Staff Only        | Delete a product.                               |
| Search Products | /products/?search=<query>       | GET    | Public            | Search products by query.                       |
| Filter Products | /products/?category=<category_id>| GET    | Public            | Filter products by category.                    |
| Create Review   | /products/<id>/review/          | POST   | Logged-in Users   | Add a review to a product.                      |
| View Reviews    | /products/<id>/reviews/         | GET    | Public            | View all reviews of a product.                  |


- Wishlist Endpoints
---

| Name                | Endpoint              | Method | Permission        | Description                                    |
|---------------------|-----------------------|--------|-------------------|------------------------------------------------|
| List Wishlist Items | /wishlist/            | GET    | Logged-in Users   | View all items in the user's wishlist.        |
| Add to Wishlist     | /wishlist/            | POST   | Logged-in Users   | Add a product to the wishlist.                |
| Delete Wishlist Item| /wishlist/<id>/       | DELETE | Logged-in Users   | Remove a product from the wishlist.           |


---
## How to Contribute

1. Fork the repository.
2. Create a new feature branch: 
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes: 
   ```bash
   git commit -m 'Add some feature'.
   ```
4. Push to the branch: 
   ```bash
   git push origin feature-name.
   ```
5. Open a pull request.

---

## License
### This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Author
- Robiul Sunny Emon
- GitHub: robiulsunnyemon
- Email: robiulsunyemon@gmail.com
