from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):

    def test_modified_settings(self):
        with self.settings(pychatbot={'name': 'Jim'}):
            self.assertIn('name', settings.pychatbot)
            self.assertEqual('Jim', settings.pychatbot['name'])

