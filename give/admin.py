from django.contrib import admin
from .models import giveaway
from django_summernote.admin import SummernoteModelAdmin


@admin.register(giveaway)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('created_at', 'email', 'answer')