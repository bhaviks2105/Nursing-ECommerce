# 🏥 GreenCart

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0+-purple.svg)
![License](https://img.shields.io/badge/License-Academic-orange.svg)

**A comprehensive e-commerce platform designed specifically for nursing and healthcare products**

[Features](#features) • [Technologies](#technologies-used) • [Installation](#installation) • [Usage](#usage) • [Screenshots](#screenshots)

</div>

# 🌿 GreenCart - Plant Nursery eCommerce Platform

**Bring nature home with GreenCart - Your online plant paradise**

A full-stack plant nursery eCommerce platform built with Django, 
featuring real-time order tracking, secure payments, and a 
beautiful catalog of plants, seeds, and gardening supplies.

🌱 Browse Plants | 🛒 Easy Checkout | 📦 Real-time Tracking | 💳 Secure Payments

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Security Features](#security-features)
- [Performance Optimizations](#performance-optimizations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About the Project

**Nursing eCommerce** is a full-stack web application developed as an academic project at **LJ University** (September 2023 - March 2024). This platform is specifically designed to facilitate the buying and selling of nursing and healthcare-related products, providing a seamless shopping experience for healthcare professionals, students, and institutions.

### 🎯 Project Objectives

- Create a user-friendly platform for purchasing nursing supplies and medical equipment
- Implement secure payment processing with industry-standard encryption
- Provide real-time order tracking and status updates
- Ensure scalability and performance through optimized database management
- Deliver a responsive design that works across all devices

### 🏆 Academic Context

This project was developed as part of the curriculum at LJ University to demonstrate:
- Full-stack web development capabilities
- Understanding of e-commerce business logic
- Implementation of security best practices
- Database design and optimization
- Real-time communication technologies

---

## ✨ Features

### 🛒 **Core E-Commerce Functionality**

- **Product Catalog Management**
  - Browse products by categories (Medical Equipment, Nursing Supplies, Educational Materials, etc.)
  - Advanced search and filtering options
  - Product details with high-quality images and descriptions
  - Stock availability indicators
  - Related product recommendations

- **User Account Management**
  - User registration and authentication
  - Profile management with order history
  - Wishlist and favorites
  - Address book for multiple shipping addresses
  - Password reset functionality

- **Shopping Cart & Checkout**
  - Add/remove items with quantity selection
  - Dynamic price calculation with tax and shipping
  - Coupon and discount code support
  - Guest checkout option
  - Save cart for later

### 💳 **Secure Payment Processing**

- **UPI Integration**
  - Multiple UPI payment gateway support
  - QR code generation for quick payments
  - Payment verification and confirmation
  - Transaction history and receipts

- **Payment Security**
  - End-to-end encryption for all transactions
  - PCI DSS compliance standards
  - Secure token-based payment processing
  - No storage of sensitive card/UPI data
  - SSL/TLS encryption for data in transit

### 📦 **Order Management System**

- **Real-Time Order Tracking**
  - WebSocket-based instant updates
  - Order status notifications (Placed → Processing → Shipped → Delivered)
  - Estimated delivery date calculations
  - SMS/Email notifications at each stage
  - Interactive tracking timeline

- **Order Features**
  - Order cancellation and modification (before shipping)
  - Return and refund requests
  - Invoice generation and download
  - Reorder previous purchases

### 📊 **Inventory Management**

- **Structured Inventory System**
  - Real-time stock level monitoring
  - Automatic low-stock alerts
  - Product categorization and tagging
  - Batch and expiry date tracking (for medical products)
  - Quality assurance checks

- **Admin Dashboard**
  - Product CRUD operations
  - Stock level management
  - Sales analytics and reports
  - Customer management
  - Order fulfillment tracking

### ⚡ **Performance & Scalability**

- **Database Optimization**
  - Indexed queries for faster data retrieval
  - Efficient database schema design
  - Query optimization and caching
  - Pagination for large datasets

- **Load Balancing**
  - Configured for local deployment with load distribution
  - Session management across multiple instances
  - Static file serving optimization
  - CDN-ready architecture

### 📱 **Responsive Design**

- **Bootstrap Framework**
  - Mobile-first responsive design
  - Cross-browser compatibility
  - Touch-friendly interface
  - Adaptive layouts for all screen sizes

---

## 🛠️ Technologies Used

### **Backend**

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Core programming language |
| Django | 4.0+ | Web framework |
| Django REST Framework | 3.14+ | API development |
| SQLite/PostgreSQL | - | Database management |
| WebSocket (Django Channels) | 4.0+ | Real-time communication |
| Celery | 5.2+ | Asynchronous task processing |

### **Frontend**

| Technology | Version | Purpose |
|------------|---------|---------|
| HTML5 | - | Markup language |
| CSS3 | - | Styling |
| Bootstrap | 5.0+ | UI framework |
| JavaScript (ES6+) | - | Client-side scripting |
| jQuery | 3.6+ | DOM manipulation |
| AJAX | - | Asynchronous requests |

### **Payment Integration**

- UPI Payment Gateways
- Razorpay API (or similar)
- Payment encryption libraries

### **Real-Time Features**

- Django Channels
- WebSocket protocol
- Redis (message broker)

### **Development Tools**

- Git & GitHub (Version control)
- VS Code / PyCharm (IDE)
- Postman (API testing)
- Chrome DevTools (Debugging)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
│  (Web Browser - Desktop/Mobile with Bootstrap Responsive UI)│
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTPS
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Django Web Server                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Views      │  │  Templates   │  │  Static Files│      │
│  │  (Business   │  │   (HTML/CSS) │  │  (JS/Images) │      │
│  │   Logic)     │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │
           ┌───────────┼───────────┐
           │           │           │
           ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌──────────────┐
    │ Database │ │WebSocket │ │Payment Gateway│
    │(SQLite/  │ │ Server   │ │  (UPI APIs)   │
    │Postgres) │ │ (Redis)  │ │               │
    └──────────┘ └──────────┘ └──────────────┘
```

---

## 📥 Installation

### **Prerequisites**

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/bhaviks2105/GreenCart
cd GreenCart
```

### **Step 2: Create Virtual Environment**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3

# Payment Gateway (Example: Razorpay)
RAZORPAY_KEY_ID=your-key-id
RAZORPAY_KEY_SECRET=your-key-secret

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Redis Configuration (for WebSocket)
REDIS_HOST=localhost
REDIS_PORT=6379
```

### **Step 5: Run Database Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Step 6: Create Superuser (Admin)**

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### **Step 7: Load Sample Data (Optional)**

```bash
python manage.py loaddata sample_data.json
```

### **Step 8: Run the Development Server**

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

### **Step 9: Run WebSocket Server (For Real-Time Features)**

In a separate terminal:

```bash
python manage.py runserver 0.0.0.0:8000
# Or use Daphne for production
daphne -b 0.0.0.0 -p 8000 nursing_ecommerce.asgi:application
```

---

## 🚀 Usage

### **For Customers:**

1. **Register/Login**
   - Create a new account or login with existing credentials
   - Complete your profile with shipping address

2. **Browse Products**
   - Navigate through categories
   - Use search and filters to find specific products
   - View detailed product information

3. **Add to Cart**
   - Select quantity and add products to cart
   - Review cart and proceed to checkout

4. **Checkout & Payment**
   - Enter shipping details
   - Choose payment method (UPI)
   - Complete secure payment

5. **Track Order**
   - View order status in real-time
   - Receive notifications for status updates
   - Download invoice

### **For Administrators:**

1. **Access Admin Panel**
   - Navigate to: `http://127.0.0.1:8000/admin/`
   - Login with superuser credentials

2. **Manage Products**
   - Add/Edit/Delete products
   - Update inventory levels
   - Set pricing and discounts

3. **Process Orders**
   - View new orders
   - Update order status
   - Manage shipping and delivery

4. **View Analytics**
   - Sales reports
   - Customer analytics
   - Inventory status

---

## 📁 Project Structure

```
Nursing-eCommerc/
│
├── nusering/                    # Main Django app
│   ├── migrations/              # Database migrations
│   ├── media/                   # User-uploaded files
│   │   ├── products/            # Product images
│   │   ├── profiles/            # User profile pictures
│   │   └── invoices/            # Generated invoices
│   ├── static/                  # Static files
│   │   ├── css/                 # Stylesheets
│   │   ├── js/                  # JavaScript files
│   │   └── images/              # Static images
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Homepage
│   │   ├── products/            # Product templates
│   │   ├── cart/                # Cart templates
│   │   ├── checkout/            # Checkout templates
│   │   └── orders/              # Order templates
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # URL routing
│   ├── forms.py                 # Django forms
│   ├── admin.py                 # Admin configuration
│   ├── consumers.py             # WebSocket consumers
│   └── manage.py                # Django management script
│
├── nursing_ecommerce/           # Project settings
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── asgi.py                  # ASGI configuration
│   └── wsgi.py                  # WSGI configuration
│
├── static/                      # Collected static files
├── media/                       # Uploaded media files
├── .gitignore                   # Git ignore file
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── manage.py                    # Django CLI
└── db.sqlite3                   # SQLite database (development)
```

---

## 🗄️ Database Schema

### **Key Models:**

#### **User Model (Extended)**
```python
- id (PK)
- username
- email
- password (hashed)
- first_name
- last_name
- phone_number
- is_verified
- created_at
- updated_at
```

#### **Product Model**
```python
- id (PK)
- name
- description
- category (FK)
- price
- discount_price
- stock_quantity
- image
- sku
- is_active
- created_at
- updated_at
```

#### **Order Model**
```python
- id (PK)
- user (FK)
- order_number
- total_amount
- status (Pending/Processing/Shipped/Delivered/Cancelled)
- payment_status
- payment_method
- shipping_address (FK)
- created_at
- updated_at
```

#### **OrderItem Model**
```python
- id (PK)
- order (FK)
- product (FK)
- quantity
- price
- subtotal
```

#### **Payment Model**
```python
- id (PK)
- order (FK)
- transaction_id
- payment_method
- amount
- status
- payment_date
- encrypted_data
```

---

## 🔒 Security Features

### **Implemented Security Measures:**

1. **Authentication & Authorization**
   - Django's built-in authentication system
   - Password hashing with PBKDF2
   - CSRF protection on all forms
   - Session management with secure cookies

2. **Payment Security**
   - End-to-end encryption for payment data
   - No storage of sensitive payment information
   - PCI DSS compliance guidelines followed
   - Secure token-based payment processing
   - SSL/TLS encryption enforced

3. **Data Protection**
   - SQL injection prevention (Django ORM)
   - XSS protection with template escaping
   - Input validation and sanitization
   - Rate limiting on API endpoints

4. **Privacy**
   - GDPR-compliant data handling
   - User consent for data collection
   - Right to data deletion
   - Encrypted database fields for sensitive data

---

## ⚡ Performance Optimizations

### **Database Level:**
- Indexed frequently queried fields (product name, category, order status)
- Query optimization with `select_related()` and `prefetch_related()`
- Database connection pooling
- Efficient pagination for large datasets

### **Application Level:**
- Django caching framework (Redis-backed)
- Template fragment caching
- Static file compression and minification
- Lazy loading for images

### **Server Level:**
- Load balancing configuration (local deployment)
- Gzip compression for responses
- CDN-ready static file serving
- Asynchronous task processing with Celery

---

## 🔮 Future Enhancements

### **Planned Features:**

- [ ] Multi-vendor marketplace functionality
- [ ] AI-powered product recommendations
- [ ] Mobile application (React Native/Flutter)
- [ ] Advanced analytics dashboard
- [ ] Integration with more payment gateways
- [ ] Subscription-based product delivery
- [ ] Live chat support with healthcare professionals
- [ ] Product review and rating system with image uploads
- [ ] Wishlist sharing and gift registry
- [ ] Multi-language support
- [ ] Progressive Web App (PWA) capabilities
- [ ] Voice search functionality
- [ ] AR product preview for medical equipment
- [ ] Integration with hospital procurement systems
- [ ] Bulk ordering for institutions

---

## 🤝 Contributing

Contributions are welcome! This is an academic project, but suggestions and improvements are appreciated.

### **How to Contribute:**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### **Contribution Guidelines:**

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PR

---

## 📄 License

This project is an **Academic Project** developed at LJ University. 

**For Educational Purposes Only**

© 2023-2024 Bhavik S. All rights reserved.

---

**Project Link:** [https://github.com/bhaviks2105/Nursing-eCommerc](https://github.com/bhaviks2105/Nursing-eCommerc)

---

## 🙏 Acknowledgments
- **Django Community** - For excellent documentation and support
- **Bootstrap Team** - For the responsive framework
- **Open Source Contributors** - For various libraries and tools used

---

