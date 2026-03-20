from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']

admin.site.register(ContactMessage, ContactMessageAdmin)