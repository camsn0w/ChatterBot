from tests.base_case import ChatBotTestCase


class StringInitializationTestCase(ChatBotTestCase):

    def get_kwargs(self):
        return {
            'storage_adapter': 'pychatbot.storage.SQLStorageAdapter',
            'database_uri': None
        }

    def test_storage_initialized(self):
        from pychatbot.storage import SQLStorageAdapter
        self.assertTrue(isinstance(self.chatbot.storage, SQLStorageAdapter))

    def test_logic_initialized(self):
        from pychatbot.logic import BestMatch
        self.assertEqual(len(self.chatbot.logic_adapters), 1)
        self.assertTrue(isinstance(self.chatbot.logic_adapters[0], BestMatch))


class DictionaryInitializationTestCase(ChatBotTestCase):

    def get_kwargs(self):
        return {
            'storage_adapter': {
                'import_path': 'pychatbot.storage.SQLStorageAdapter',
                'database_uri': None
            },
            'logic_adapters': [
                {
                    'import_path': 'pychatbot.logic.BestMatch',
                },
                {
                    'import_path': 'pychatbot.logic.MathematicalEvaluation',
                }
            ]
        }

    def test_storage_initialized(self):
        from pychatbot.storage import SQLStorageAdapter
        self.assertTrue(isinstance(self.chatbot.storage, SQLStorageAdapter))

    def test_logic_initialized(self):
        from pychatbot.logic import BestMatch
        from pychatbot.logic import MathematicalEvaluation
        self.assertEqual(len(self.chatbot.logic_adapters), 2)
        self.assertTrue(isinstance(self.chatbot.logic_adapters[0], BestMatch))
        self.assertTrue(isinstance(self.chatbot.logic_adapters[1], MathematicalEvaluation))
