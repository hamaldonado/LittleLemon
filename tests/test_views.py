from django.test import TestCase
from restaurant.models import Menu
from rest_framework.renderers import JSONRenderer
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        item_1 = Menu.objects.create(title="Pan con Pollo", price=8, inventory=10) 
        item_2 = Menu.objects.create(title="Pan con Huevo", price=4, inventory=10)
        item_3 = Menu.objects.create(title="Pan con Palta", price=3, inventory=10)
        item_4 = Menu.objects.create(title="Pan con Mantequilla", price=2, inventory=10)
    
    def test_getall(self):
        items = Menu.objects.all()
        expected = JSONRenderer().render([
            {
                'title': 'Pan con Pollo',
                'price': '8.00',
                'inventory': 10
            },
            {
                'title': 'Pan con Huevo',
                'price': '4.00',
                'inventory': 10
            },
            {
                'title': 'Pan con Palta',
                'price': '3.00',
                'inventory': 10
            },
            {
                'title': 'Pan con Mantequilla',
                'price': '2.00',
                'inventory': 10
            }
        ])

        serialized_data = MenuSerializer(items, many=True).data
        json_text = JSONRenderer().render(serialized_data)

        self.assertEqual(json_text, expected)

