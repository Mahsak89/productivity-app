from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task, Category


class TaskListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='flip', password='pass')
        self.category = Category.objects.create(
            owner=self.user, name='Test Category')

    def test_can_list_tasks(self):
        Task.objects.create(
            owner=self.user, category=self.category, title='A Task')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
