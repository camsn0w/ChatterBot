from django.contrib import admin
from pychatbot.ext.django_pychatbot.model_admin import StatementAdmin, TagAdmin
from pychatbot.ext.django_pychatbot.models import Statement, Tag


admin.site.register(Statement, StatementAdmin)
admin.site.register(Tag, TagAdmin)
