from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Pasta", price=120, inventory=60)

    def test_get_all(self):
        # Initialize the test client
        client = APIClient()

        # Send GET request to retrieve all Menu items
        response = client.get('/restaurant/menu/')  # Adjust this URL if necessary

        # Assert the response status is OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response data contains the serialized items correctly
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Pizza')
        self.assertEqual(response.data[1]['title'], 'Pasta')
