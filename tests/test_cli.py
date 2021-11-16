from unittest import TestCase
from pychatbot import __main__ as main


class CommandLineInterfaceTests(TestCase):
    """
    Tests for the command line tools that are included with pychatbot.
    """

    def test_get_pychatbot_version(self):
        version = main.get_pychatbot_version()
        version_parts = version.split('.')
        self.assertEqual(len(version_parts), 3)
        self.assertTrue(version_parts[0].isdigit())
        self.assertTrue(version_parts[1].isdigit())
