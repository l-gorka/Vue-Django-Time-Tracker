import datetime

from django.contrib.auth.models import User
from tracker.models import DayEntry, Project, TimeEntry

from .base_test_data import BaseTestCase


class TestModelsCreated(BaseTestCase):

    def test_project_is_created(self) -> None:
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.title, 'Project1')
        self.assertEqual(project.color, '#000000')

    def test_time_entry_created(self) -> None:
        entry = TimeEntry.objects.all()[0]

        self.assertEqual(entry.description, 'Some desc')

    def test_time_entry_duration_is_computed(self):
        entry = TimeEntry.objects.all()[0]

        self.assertEqual(entry.time_difference(), 3600)

    def test_day_entry_is_created_after_signal(self):
        day_entry = DayEntry.objects.all()[0]

        self.assertIsNotNone(day_entry)

    def test_day_entry_has_time_entry_in_m2m(self):
        day_entry = DayEntry.objects.all()[0]
        time_entry = TimeEntry.objects.all()[0]

        self.assertIn(time_entry, day_entry.time_entries.all())

    def test_project_has_time_entry_in_m2m(self):
        project = Project.objects.get(title='Project1')
        time_entry = TimeEntry.objects.all()[0]

        self.assertIn(time_entry, project.time_entries.all())

    def test_day_entry_has_total_time_computed(self):
        day_entry = DayEntry.objects.all()[0]

        self.assertEqual(day_entry.time_total, 3600)

    def test_project_has_total_time_computed(self):
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.time_total, 3600)


class TestTimeEntryProjectUpdate(BaseTestCase):

    def setUp(self):
        time_entry = TimeEntry.objects.all()[0]
        project2 = Project.objects.get(title='Project2')
        time_entry.project = project2
        time_entry.save()

    def test_time_entry_has_updated_project(self):
        time_entry = TimeEntry.objects.all()[0]

        self.assertEqual(time_entry.project.title, 'Project2')

    def test_project_total_time_updated(self):
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.time_total, 0)


class TimeEntryDeleted(BaseTestCase):

    def setUp(self):
        time_entry = TimeEntry.objects.all()[0]
        time_entry.delete()

    def test_time_entry_is_deleted(self):
        self.assertEqual(TimeEntry.objects.all().count(), 0)

    def test_day_entry_is_deleted(self):
        self.assertEqual(DayEntry.objects.all().count(), 0)

    def test_project_total_time_is_computed(self):
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.time_total, 0)


class TimeEntryUpdated(BaseTestCase):

    def setUp(self):
        time_entry = TimeEntry.objects.all()[0]
        time_entry.start_date = 1647106938
        time_entry.end_date = 1647114138
        time_entry.save()

    def test_time_entry_total_time_updated(self):
        time_entry = TimeEntry.objects.all()[0]
        self.assertEqual(time_entry.time_difference(), 7200)

    def test_day_entry_date_changed(self):
        day_entry = DayEntry.objects.all()[0]

        self.assertEqual(day_entry.date, datetime.date(2022, 3, 12))


class NewTimeEntryAdded(BaseTestCase):

    def setUp(self):
        entry = TimeEntry.objects.create(
            owner = User.objects.get(username='test_user'),
            description = 'Some desc',
            project = Project.objects.get(title='Project1'),
            start_date = 1647002538,
            end_date = 1647006138
        )

    def test_project_has_2_time_entries_in_m2m(self):
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.time_entries.all().count(), 2)

    def test_day_entry_has_2_time_entries_in_m2m(self):
        day_entry = DayEntry.objects.all()[0]

        self.assertEqual(day_entry.time_entries.all().count(), 2)

    def test_project_has_total_time_computed(self):
        project = Project.objects.get(title='Project1')

        self.assertEqual(project.time_total, 7200)

    def test_day_entry_has_total_time_computed(self):
        day_entry = DayEntry.objects.all()[0]

        self.assertEqual(day_entry.time_total, 7200)
