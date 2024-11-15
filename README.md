# ShopCart E-Commerce Platform

This project is a basic e-commerce platform built with Django, allowing users to browse products, register, log in, manage their cart, and explore products by category. Below is an overview of its features and functionality.

## Key Features

### 1. User Authentication
- **User Registration:** Users can sign up by creating an account. The registration form ensures that passwords and confirmation passwords match before saving user data.
- **Login and Logout:** Users can log in using their username and password. Once authenticated, they can access protected pages like their cart. Users can log out to end their session.

### 2. Product Management
- **Product Listings:** Products are organized by categories, such as Men's and Women's products. Each product includes details such as images, descriptions, and prices.
- **Product Detail View:** Users can view detailed information about individual products, including a description, price, and an "Add to Cart" option.

### 3. Shopping Cart
- **Add to Cart:** Users can add products to their shopping cart. They can also increase the quantity of items if they are already in the cart.
- **View Cart:** Users can view the contents of their cart, including the products, quantities, and the total price.
- **Remove from Cart:** Users can remove products from their cart when no longer needed.

### 4. Category Pages
- **Category Filters:** Products are grouped into categories such as Men's and Women's. Users can view the products within a specific category by selecting it.

## URL Configuration
The project includes various URLs that map to views in the application:

- **Home Page:** Displays products for different categories.
- **Authentication Routes:** Handle user registration, login, and logout.
- **Cart Routes:** Manage adding products to the cart, viewing cart contents, and removing items.
- **Category Routes:** Display products filtered by category.
- **Product Routes:** Show detailed information about individual products.

## Tech Stack
- **Frontend:** HTML, CSS (with Bootstrap for responsive design), JavaScript, and Django Templates.
- **Backend:** Django (Python framework) for server-side logic, views, and user management.
- **Database:** Django's ORM, likely with SQLite, to store user, product, and cart data.
- **Media Handling:** The project supports media files (like product images) through Django’s `MEDIA_URL` and `MEDIA_ROOT` settings.

## Extending the Platform
This e-commerce platform can be easily extended with additional features, such as:

- **Order Management:** Adding order placement, tracking, and management.
- **Payment Processing:** Integration with payment gateways for processing transactions.
- **User Profiles:** Allowing users to manage their profiles and order history.

The modular nature of the project makes it easy to manage and extend with new features over time.

### Installation
### 1.Clone the repository:

   
    git clone https://github.com/yourusername/ecommerce-platform.git

### 2. Install dependencies:


    pip install -r requirements.txt
### 3.Run migrations to set up the database:


    python manage.py migrate
### 4.Run the development server:

    python manage.py runserver
### 5.Open your browser
 and go to http://127.0.0.1:8000 to start using the platform.
### License
This project is open source and available under the **MIT** License.
