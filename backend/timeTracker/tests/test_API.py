from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .base_test_data import BaseAPITestCase
from django.contrib.auth.models import User
from tracker.models import TimeEntry, Project, DayEntry
import pdb


class TestRegistration(BaseAPITestCase):

    def test_user_can_not_register_with_empty_data(self):
        response = self.client.post(reverse('register'))
        self.assertEqual(response.data, 'Password incorrect')

    def test_user_can_not_register_with_incorrect_password(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.data, 'Password incorrect')

    def test_user_can_not_register_with_the_same_username(self):
        self.client.post(self.register_url, self.correct_register_data)
        response = self.client.post(
            self.register_url, self.correct_register_data)
        self.assertEqual(response.data, 'Username already taken')

    def test_user_can_register(self):
        response = self.client.post(
            self.register_url, self.correct_register_data)
        self.assertEqual(response.data, 'Created')


class TestLogin(BaseAPITestCase):

    def setUp(self):
        self.client.post(self.register_url, self.correct_register_data)

    def test_user_can_not_login_with_incorrect_data(self):
        response = self.client.post(self.login_url, self.incorrect_login_data)

        self.assertEqual(response.status_code, 401)

    def test_user_can_login(self):
        response = self.client.post(self.login_url, self.correct_login_data)

        self.assertEqual(response.status_code, 200)


class TestChangePassword(BaseAPITestCase):

    def setUp(self):
        user = User.objects.get(username='test_user')
        self.client.force_authenticate(user=user)

    def test_user_can_change_password(self):
        response = self.client.post(
            self.change_password_url, self.correct_change_password_data)

        self.assertEqual(response.data, 'Password changed')

    def test_user_can_not_change_password_entering_wrong_old_password(self):
        response = self.client.post(
            self.change_password_url, self.incorrect_change_password_data)

        self.assertEqual(response.data,
                         'Password you entered is incorrect. Please retype your current password.')


class TestTimeEntry(BaseAPITestCase):

    def setUp(self):
        user = User.objects.get(username='test_user')
        self.client.force_authenticate(user=user)

    def test_user_can_fetch_time_entries(self):
        response = self.client.get(self.time_entries_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], self.entry.id)

    def test_user_can_create_time_entry(self):
        response = self.client.post(self.time_entry_create_url, self.time_entry_data)

        self.assertEqual(response.status_code, 200)

    def test_user_can_update_time_entry(self):
        response = self.client.post(self.time_entry_update_url, self.time_entry_update_data)

        self.assertEqual(response.data['description'], 'Updated description')

    def test_user_can_delete_time_entry(self): 
        response = self.client.post(self.time_entry_delete_url)

        self.assertEqual(response.status_code, 202)
        self.assertEqual(TimeEntry.objects.all().count(), 0)


class TestProject(BaseAPITestCase):
    
    def setUp(self):
        user = User.objects.get(username='test_user')
        self.client.force_authenticate(user=user)

    def test_user_can_fetch_projects(self):
        response = self.client.get(self.projects_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], self.entry.id)

    def test_user_can_create_project(self):
        response = self.client.post(self.project_create_url, self.project_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Project3')

    def test_user_can_update_project(self):
        response = self.client.post(self.project_update_url, self.project_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Project3')

    def test_user_can_delete_project(self):
        response = self.client.post(self.project_delete_url)

        self.assertEqual(response.status_code, 202)
        self.assertEqual(Project.objects.all().count(), 0)

class TestDayEntries(BaseAPITestCase):

    def setUp(self):
        user = User.objects.get(username='test_user')
        self.client.force_authenticate(user=user)

    def test_user_can_fetch_day_entries(self):
        response = self.client.get(self.day_entires_url)
        print(DayEntry.objects.all())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], 2)