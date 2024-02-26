from django.contrib import admin
from .models import contact
from django_summernote.admin import SummernoteModelAdmin



@admin.register(contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('created_at', 'email', 'subject', 'message')