from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class TestAPI(APITestCase):

    def setUp(self):
        self.user = self.setup_user()
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.URL = 'http://127.0.0.1:8000/api/'
        self.auth = {'Authorization': f'Token {self.token}'}

	@staticmethod
	def setup_user():
		User = get_user_model()
		return User.objects.create_user(
			email='test@simple.com',
			password='testing123',
			type='shop',
			is_active=1,
			is_staff=1
		)

	def test_user_detail(self):
		method = '/api/user/details'
		response = self.client.get(path=method, **self.auth)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_change_user_details(self):
		method = '/api/user/details'
		params = {'first_name': 'Хулио',
				   'last_name': 'Петренко'}
		response = self.client.post(path=method, data=params, **self.auth)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_contacts_view(self):
		method = '/api/user/contact'
		response = self.client.get(path=method, **self.auth)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_add_contact(self):
		method = '/api/user/contact'
		params = {'city': '`Samara`',
				   'street': 'Lenina 5',
				   'phone': '+79333333333'}
		response = self.client.post(path=method, data=params, **self.auth)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_contact_change(self):
		method = '/api/user/contact'
		params = {'city': 'Berlin',
				   'street': 'Gaus street',
				   'phone': '+69999999999'}
		response = self.client.put(path=method, data=params, **self.auth)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_shop_view(self):
		method = '/api/shops'
		response = self.client.get(path=method)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_category_view(self):
		method = '/api/categories'
		response = self.client.get(path=method)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
