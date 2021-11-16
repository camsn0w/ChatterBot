from pychatbot import ChatBot
from django.test import TransactionTestCase
from tests_django import test_settings


class pychatbotTestCase(TransactionTestCase):

    def setUp(self):
        super().setUp()
        self.chatbot = ChatBot(**test_settings.pychatbot)
