
# Product Management API

## Overview
A RESTful API for managing products. This API allows users to perform CRUD (Create, Read, Update, Delete) operations on products, providing a simple interface for managing product data.

## Features
- Create, Read, Update, Delete (CRUD) operations for products.
- Swagger UI for API documentation.

## Getting Started

### Prerequisites
- Python 3
- Django
- Django REST Framework
- Any other necessary dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/muaadh-adeniyi/product-management-API.git
   ```
2. Navigate into the project directory:
   ```bash
   cd product-management-API
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API
1. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the server:
   ```bash
   python manage.py runserver
   ```
3. Access the API at `http://127.0.0.1:8000/`.

## API Documentation
- Swagger UI: Access the API documentation at `/swagger/`.
- ReDoc: Access the API documentation at `/redoc/`.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.


