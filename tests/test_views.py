from django.test import TestCase
from restaurant.models import Menu
from rest_framework.renderers import JSONRenderer
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.item_1 = Menu.objects.create(title="Pan con Pollo", price=8, inventory=10) 
        self.item_2 = Menu.objects.create(title="Pan con Huevo", price=4, inventory=10)
        self.item_3 = Menu.objects.create(title="Pan con Palta", price=3, inventory=10)
        self.item_4 = Menu.objects.create(title="Pan con Mantequilla", price=2, inventory=10)

    def test_getall(self):
        items = Menu.objects.all()
        expected_json = JSONRenderer().render([
            {
                'id': self.item_1.pk,
                'title': 'Pan con Pollo',
                'price': '8.00',
                'inventory': 10
            },
            {
                'id': self.item_2.pk,
                'title': 'Pan con Huevo',
                'price': '4.00',
                'inventory': 10
            },
            {
                'id': self.item_3.pk,
                'title': 'Pan con Palta',
                'price': '3.00',
                'inventory': 10
            },
            {
                'id': self.item_4.pk,
                'title': 'Pan con Mantequilla',
                'price': '2.00',
                'inventory': 10
            }
        ])

        serialized_data = MenuSerializer(items, many=True).data
        actual_json = JSONRenderer().render(serialized_data)

        self.assertEqual(actual_json, expected_json)

