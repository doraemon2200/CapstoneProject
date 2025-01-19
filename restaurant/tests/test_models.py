from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create an instance of the Menu model
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Assert the string representation of the instance
        self.assertEqual(str(item), "IceCream : 80")