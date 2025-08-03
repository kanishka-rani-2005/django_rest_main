# Django REST API Project

This project demonstrates a comprehensive, step-by-step implementation of **Django REST Framework (DRF)** for building robust API backends. It covers everything from installation to advanced filtering using class-based views, viewsets, nested serializers, pagination, and more.

---

## 📚 Topics Covered

### 1. Model & Serialization
- Creating Models
- Manual Serialization
- DRF Serializers

### 2. Function-Based Views (FBVs)
- GET Method
- POST: Storing Data
- GET by Primary Key
- PUT/PATCH: Update Student
- DELETE Operation

### 3. Class-Based Views (CBVs)
- CBV Introduction
- Employee Model
- Employee Serializer
- List All Employees
- Create Employee
- Retrieve Employee
- Update & Delete

### 4. Mixins
- Mixin Overview
- ListModelMixin & CreateModelMixin
- RetrieveUpdateDestroyMixin

### 5. Generics
- Generics Overview
- ListCreateAPIView
- RetrieveUpdateDestroyAPIView

### 6. Viewsets
- Viewset Introduction
- List & Create via Viewsets
- Retrieve Single Object
- ModelViewSet

### 7. Nested Serializers & Blog System
- Nested Serializers Introduction
- Blog and Comment Models
- Creating Serializers
- Nested Serializers Implementation
- Primary Key Operations

### 8. Pagination
- Pagination Overview
- Global Pagination
- Custom Pagination

### 9. Filtering
- Basic Filtering
- Custom Filter by Designation
- Filter by Name and ID
- Advanced Filtering
- SearchFilter
- OrderingFilter




## Apps

- `api/` - Core API utilities, filters, pagination, and serializers.
- `blogs/` - Handles blog-related functionalities.
- `employees/` - Manages employee records and related operations.
- `students/` - Manages student data and APIs.



## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Start the development server:

   ```bash
   python manage.py runserver
   ```
# 📣 Course Reference
    This project is part of a Django + REST API full course. It covers both foundational and            advanced   concepts, suitable for building production-grade REST APIs and scalable backends.
