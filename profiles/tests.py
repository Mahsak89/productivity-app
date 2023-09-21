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


class ProfileDetailViewTests(APITestCase):
    def test_can_retrieve_profile_using_valid_id(self):
        user = User.objects.create_user(username='flip', password='pass')
        response = self.client.get(f'/profiles/{user.id}/')
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
