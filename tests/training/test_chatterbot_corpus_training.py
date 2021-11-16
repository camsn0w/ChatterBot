from tests.base_case import ChatBotTestCase
from pychatbot.trainers import pychatbotCorpusTrainer


class pychatbotCorpusTrainingTestCase(ChatBotTestCase):
    """
    Test case for training with data from the pychatbot Corpus.

    Note: This class has a mirror tests_django/integration_tests/
    """

    def setUp(self):
        super().setUp()
        self.trainer = pychatbotCorpusTrainer(
            self.chatbot,
            show_training_progress=False
        )

    def test_train_with_english_greeting_corpus(self):
        self.trainer.train('pychatbot.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)

    def test_train_with_english_greeting_corpus_search_text(self):
        self.trainer.train('pychatbot.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)
        self.assertEqual(results[0].search_text, 'hello')

    def test_train_with_english_greeting_corpus_search_in_response_to(self):
        self.trainer.train('pychatbot.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(in_response_to='Hello'))

        self.assertGreater(len(results), 1)
        self.assertEqual(results[0].search_in_response_to, 'hello')

    def test_train_with_english_greeting_corpus_tags(self):
        self.trainer.train('pychatbot.corpus.english.greetings')

        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)
        statement = results[0]
        self.assertEqual(['greetings'], statement.get_tags())

    def test_train_with_multiple_corpora(self):
        self.trainer.train(
            'pychatbot.corpus.english.greetings',
            'pychatbot.corpus.english.conversations',
        )
        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)

    def test_train_with_english_corpus(self):
        self.trainer.train('pychatbot.corpus.english')
        results = list(self.chatbot.storage.filter(text='Hello'))

        self.assertGreater(len(results), 1)
