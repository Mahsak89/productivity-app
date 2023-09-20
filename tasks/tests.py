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

    def test_logged_in_user_can_create_task(self):
        self.client.login(username='flip', password='pass')
        response = self.client.post('/tasks/', {
            'owner': self.user.id,
            'category': self.category.id,
            'title': 'A Task',
            'description': 'Description of the task',
            'deadline': '2023-09-30T12:00:00Z',
            'state': 'Open',
            'priority': 'Medium'
        })
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_task(self):
        response = self.client.post('/tasks/', {
            'owner': self.user.id,
            'category': self.category.id,
            'title': 'A Task',
            'description': 'Description of the task',
            'deadline': '2023-09-30T12:00:00Z',
            'state': 'Open',
            'priority': 'Medium'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='flip', password='pass')
        self.category = Category.objects.create(
            owner=self.user, name='Test Category')
        self.task = Task.objects.create(
            owner=self.user,
            category=self.category,
            title='A Task',
            description='Description of the task',
            deadline='2023-09-30T12:00:00Z',
            state='Open',
            priority='Medium'
        )

    def test_can_retrieve_task_using_valid_id(self):
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.data['title'], 'A Task')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_task_using_invalid_id(self):
        response = self.client.get('/tasks/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_task(self):
        self.client.login(username='flip', password='pass')
        response = self.client.put('/tasks/1/', {
            'owner': self.user.id,
            'category': self.category.id,
            'title': 'Updated Task',
            'description': 'Updated description',
            'deadline': '2023-09-30T12:00:00Z',
            'state': 'Open',
            'priority': 'Medium'
        })
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_task(self):
        suzi = User.objects.create_user(username='suzi', password='pass')
        category_suzi = Category.objects.create(
            owner=suzi, name='Another Category')
        task_suzi = Task.objects.create(
            owner=suzi,
            category=category_suzi,
            title='Another Task',
            description='Description of another task',
            deadline='2023-09-30T12:00:00Z',
            state='Open',
            priority='Medium'
        )
        self.client.login(username='flip', password='pass')
        response = self.client.put(f'/tasks/{task_suzi.id}/', {
            'owner': suzi.id,
            'category': category_suzi.id,
            'title': 'Updated Task',
            'description': 'Updated description',
            'deadline': '2023-09-30T12:00:00Z',
            'state': 'Open',
            'priority': 'Medium'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
