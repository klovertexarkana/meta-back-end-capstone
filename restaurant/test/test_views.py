from django.test import TestCase
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from restaurant.models import *
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=1, title='Steak', price=10.00, inventory=15)
        Menu.objects.create(id=2, title='Baklava', price=4.00, inventory=100)
        Menu.objects.create(id=3, title='Spanakopita', price=6.00, inventory=25)

        self.user = User.objects.create_user(
            username="testUser",
            password="testPassword",
        )
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.login(username='testUser', password='testPassword')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        counter = 1
        for item in response.data:
            self.assertEqual(item == {'title': Menu.objects.get(id=counter).title, 'price': str(Menu.objects.get(id=counter).price), 
                                 'inventory': Menu.objects.get(id=counter).inventory}, True)
            counter += 1

