from django.contrib import admin

from .models import Question
from .models import Choice


admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Administration"
admin.site.index_title = "Welcome to Polls Admin Panel"

admin.site.register(Question)
admin.site.register(Choice)