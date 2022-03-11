from django.test import TestCase
from tracker.models import TimeEntry, Project, DayEntry
from django.contrib.auth.models import User


class BaseTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # create user for tests
        user = User.objects.create_user(
            username = 'test_user',
            email = 'test_user@test.it',
            password = 'test4321'
        )
        # create 2 project objects
        project1 = Project.objects.create(
            owner = User.objects.all()[0],
            title = 'Project1',
            color = '#000000',
        )
        project2 = Project.objects.create(
            owner = User.objects.all()[0],
            title = 'Project2',
            color = '#000000',
        )
        #create time entry
        entry = TimeEntry.objects.create(
            owner = User.objects.get(username='test_user'),
            description = 'Some desc',
            project = Project.objects.get(title='Project1'),
            start_date = 1647016938,
            end_date = 1647020538
        )
        super().setUpTestData()