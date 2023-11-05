from django.test import TestCase
from restaurant.models import Menu, Table

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Hamburger", price=14, inventory=20)
        self.assertEqual(str(item), "Hamburger : 14")

class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Table.objects.create(name="Steve", no_of_guests=6, booking_date="2023-11-05")
        self.assertEquals(str(booking), "Steve : 2023-11-05")
        