from pychatbot import ChatBot
from pychatbot.adapters import Adapter
from tests.base_case import ChatBotTestCase


class AdapterValidationTests(ChatBotTestCase):

    def test_invalid_storage_adapter(self):
        kwargs = self.get_kwargs()
        kwargs['storage_adapter'] = 'pychatbot.logic.LogicAdapter'
        with self.assertRaises(Adapter.InvalidAdapterTypeException):
            self.chatbot = ChatBot('Test Bot', **kwargs)

    def test_valid_storage_adapter(self):
        kwargs = self.get_kwargs()
        kwargs['storage_adapter'] = 'pychatbot.storage.SQLStorageAdapter'
        try:
            self.chatbot = ChatBot('Test Bot', **kwargs)
        except Adapter.InvalidAdapterTypeException:
            self.fail('Test raised InvalidAdapterException unexpectedly!')

    def test_invalid_logic_adapter(self):
        kwargs = self.get_kwargs()
        kwargs['logic_adapters'] = ['pychatbot.storage.StorageAdapter']
        with self.assertRaises(Adapter.InvalidAdapterTypeException):
            self.chatbot = ChatBot('Test Bot', **kwargs)

    def test_valid_logic_adapter(self):
        kwargs = self.get_kwargs()
        kwargs['logic_adapters'] = ['pychatbot.logic.BestMatch']
        try:
            self.chatbot = ChatBot('Test Bot', **kwargs)
        except Adapter.InvalidAdapterTypeException:
            self.fail('Test raised InvalidAdapterException unexpectedly!')

    def test_valid_adapter_dictionary(self):
        kwargs = self.get_kwargs()
        kwargs['storage_adapter'] = {
            'import_path': 'pychatbot.storage.SQLStorageAdapter'
        }
        try:
            self.chatbot = ChatBot('Test Bot', **kwargs)
        except Adapter.InvalidAdapterTypeException:
            self.fail('Test raised InvalidAdapterException unexpectedly!')

    def test_invalid_adapter_dictionary(self):
        kwargs = self.get_kwargs()
        kwargs['storage_adapter'] = {
            'import_path': 'pychatbot.logic.BestMatch'
        }
        with self.assertRaises(Adapter.InvalidAdapterTypeException):
            self.chatbot = ChatBot('Test Bot', **kwargs)
