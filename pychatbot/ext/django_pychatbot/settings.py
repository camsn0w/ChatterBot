"""
Default pychatbot settings for Django.
"""
from django.conf import settings
from pychatbot import constants


pychatbot_SETTINGS = getattr(settings, 'pychatbot', {})

pychatbot_DEFAULTS = {
    'name': 'pychatbot',
    'storage_adapter': 'pychatbot.storage.DjangoStorageAdapter',
    'django_app_name': constants.DEFAULT_DJANGO_APP_NAME
}

pychatbot = pychatbot_DEFAULTS.copy()
pychatbot.update(pychatbot_SETTINGS)
