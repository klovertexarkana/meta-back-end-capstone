from django.test import TestCase
from restaurant.models import *

class MenuTestCase(TestCase):

    def setUp(self):
        self.item = Menu.objects.create(id=1, title="Ice Cream", price=5.00, inventory=100);
        Menu.objects.create(id=2, title="Pizza", price=10.00, inventory=10)
        Menu.objects.create(id=3, title="Burger", price=5.00, inventory=20)

    def test_get_item(self):
        self.assertEqual(str(self.item), "Ice Cream : 5.0")

    def test_menu_items(self):
        pizza = Menu.objects.get(title="Pizza")
        burger = Menu.objects.get(title="Burger")
        self.assertEqual(pizza.price, 10.00)
        self.assertEqual(burger.price, 5.00)
        self.assertEqual(pizza.inventory, 10)
        self.assertEqual(burger.inventory, 20)