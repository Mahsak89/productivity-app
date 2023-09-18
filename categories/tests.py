from django.contrib.auth.models import User
from .models import Category
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='flip', password='pass')

    def test_can_list_categories(self):
        flip = User.objects.get(username='flip')
        Category.objects.create(owner=flip, name='a name')
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_category(self):
        self.client.login(username='flip', password='pass')
        response = self.client.post('/categories/', {'name': 'a name'})
        count = Category.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_category(self):
        response = self.client.post('/categories/', {'name': 'a name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CategoryDetailViewTests(APITestCase):
    def setUp(self):
        flip = User.objects.create_user(username='flip', password='pass')
        suzi = User.objects.create_user(username='suzi', password='pass')
        Category.objects.create(
            owner=flip, name='a name'
        )
        Category.objects.create(
            owner=suzi, name='another name'
        )

    def test_can_retrieve_category_using_valid_id(self):
        response = self.client.get('/categories/1/')
        self.assertEqual(response.data['name'], 'a name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_category_using_invalid_id(self):
        response = self.client.get('/categories/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_category(self):
        self.client.login(username='flip', password='pass')
        response = self.client.put('/categories/1/', {'name': 'a new name'})
        category = Category.objects.filter(pk=1).first()
        self.assertEqual(category.name, 'a new name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_category(self):
        self.client.login(username='flip', password='pass')
        response = self.client.put('/categories/2/', {'name': 'a new name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_category(self):
        self.client.login(username='flip', password='pass')
        response = self.client.delete('/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count = Category.objects.count()
        self.assertEqual(count, 1)

    def test_user_cant_delete_another_users_category(self):
        self.client.login(username='flip', password='pass')
        response = self.client.delete('/categories/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Category.objects.count()
        self.assertEqual(count, 2)
