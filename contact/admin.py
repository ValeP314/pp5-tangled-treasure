from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_message')


admin.site.register(Contact, ContactAdmin)
