from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile


class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='flip', password='pass')

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
