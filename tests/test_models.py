from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Hamburger", price=14, inventory=20)
        self.assertEqual(str(item), "Hamburger : 14")