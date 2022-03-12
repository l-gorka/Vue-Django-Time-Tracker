import imp
from django.test import TestCase
from tracker.models import TimeEntry, Project, DayEntry
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        user = User.objects.create_user(
            username='test_user',
            email='test_user@test.it',
            password='test4321'
        )

        project1 = Project.objects.create(
            owner=User.objects.all()[0],
            title='Project1',
            color='#000000',
        )
        project2 = Project.objects.create(
            owner=User.objects.all()[0],
            title='Project2',
            color='#000000',
        )

        entry = TimeEntry.objects.create(
            owner=User.objects.get(username='test_user'),
            description='Some desc',
            project=Project.objects.get(title='Project1'),
            start_date=1647016938,
            end_date=1647020538
        )
        super().setUpTestData()


class BaseAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            email='test_user@test.it',
            password='test4321'
        )
        cls.project1 = Project.objects.create(
            owner=User.objects.all()[0],
            title='Project1',
            color='#000000',
        )
        cls.entry = TimeEntry.objects.create(
            owner=User.objects.get(username='test_user'),
            description='Some desc',
            project=Project.objects.get(title='Project1'),
            start_date=1647016938,
            end_date=1647020538
        )
        cls.register_url = reverse('register')
        cls.login_url = reverse('token_obtain_pair')
        cls.change_password_url = reverse('password-change')

        cls.time_entry_create_url = reverse('time-entry-create')
        cls.time_entry_update_url = reverse('time-entry-update', args=(cls.entry.id,))
        cls.time_entry_delete_url = reverse('time-entry-delete', args=(cls.entry.id,))
        cls.time_entries_url = reverse('time-entries')

        cls.projects_url = reverse('project-list')
        cls.project_update_url = reverse('project-update', args=(cls.project1.id,))
        cls.project_delete_url = reverse('project-delete', args=(cls.project1.id,))
        cls.project_create_url = reverse('project-create')

        cls.day_entires_url = reverse('day-entries')

        cls.correct_register_data = {
            'username': 'test',
            'email': 'email@email.pl',
            'password': 'trolol012'
        }
        cls.short_password_data = {
            'username': 'test',
            'email': 'email@email.pl',
            'password': 'trolo'
        }
        
        cls.incorrect_login_data = {
            'username': 'test',
            'password': 'wrong_pass123'
        }
        cls.correct_login_data = {
            'username': 'test',
            'password': 'trolol012'
        }

        cls.correct_change_password_data = {
            'old_password': 'test4321',
             'password': 'testtest4321',
            'password2': 'testtest4321'
        }
        cls.incorrect_change_password_data = {
            'old_password': 'wrong_old_password',
             'password': 'testtest4321',
            'password2': 'testtest4321'
        }
        cls.time_entry_data = {
            'owner': User.objects.get(username='test_user'),
            'description':'Some desc',
            'project': Project.objects.get(title='Project1'),
            'start_date': 1647016938,
            'end_date':1647020538
        }
        cls.time_entry_update_data = {
            'owner': User.objects.get(username='test_user'),
            'description':'Updated description',
            'project': Project.objects.get(title='Project1'),
            'start_date': 1647016938,
            'end_date':1647020538
        }
        cls.project_data = {
            'owner': cls.user.id,
            'title': 'Project3',
            'color': '#342fe3'
        }
        super().setUpTestData()
