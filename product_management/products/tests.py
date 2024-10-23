from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

class ProductHandlerTestCase(APITestCase):

    def setUp(self):
        # Set up initial test product data
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            currency="USD"
        )
        self.valid_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 20.00,
            "currency": "USD"
        }
        self.update_data = {
            "id": self.product.id,
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 25.00,
            "currency": "USD"
        }

    def test_create_product(self):
        # Test creating a new product (POST)
        response = self.client.post(reverse('product_handler'), self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Product")

    def test_retrieve_product_by_id(self):
        # Test retrieving a product by ID (GET)
        url = f"{reverse('product_handler')}?id={self.product.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_retrieve_product_by_name(self):
        # Test retrieving a product by name (GET)
        url = f"{reverse('product_handler')}?name={self.product.name}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        # Test updating a product (PUT)
        response = self.client.put(reverse('product_handler'), self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Product")

    def test_delete_product_by_id(self):
        # Test deleting a product by ID (DELETE)
        response = self.client.delete(reverse('product_handler'), {"id": self.product.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product_by_name(self):
        # Test deleting a product by name (DELETE)
        response = self.client.delete(reverse('product_handler'), {"name": self.product.name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


