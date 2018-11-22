import os
from django.urls import reverse
from django.test import TestCase, Client
from rest_framework import status
from mixer.backend.django import mixer
from ..models import *


class TestUpload(TestCase):

    def setUp(self):
        self.username, self.password = 'user', 'pass'
        self.client = Client()
        self.filepath = os.path.join(os.path.dirname(__file__), 'data/test.csv')

    def create_user(self):
        user = User.objects.create_user(username=self.username, password=self.password)

        return user

    def create_superuser(self):
        user = User.objects.create_superuser(username=self.username,
                                             password=self.password,
                                             email='hoge@example.com')
        return user

    def create_project(self):
        project = mixer.blend('server.Project')

        return project

    def test_create_doc_by_admin(self):
        """
        Ensure we can create a new document object by admin.
        """
        user = self.create_superuser()
        project = self.create_project()
        project.users.add(user)

        with open(self.filepath) as f:
            url = reverse('upload', args=[project.id])
            self.client.login(username=self.username, password=self.password)
            response = self.client.post(url, {'csv_file': f})

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Document.objects.count(), 3)

    def test_create_doc_by_user(self):
        """
        Ensure we cannot create a new project object by user.
        """
        user = self.create_user()
        project = self.create_project()
        project.users.add(user)

        with open(self.filepath) as f:
            url = reverse('upload', args=[project.id])
            self.client.login(username=self.username, password=self.password)
            response = self.client.post(url, {'csv_file': f})

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Document.objects.count(), 0)
