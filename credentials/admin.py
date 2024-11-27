from django.contrib import admin
from .models import Credentials

@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ('name_account', 'email_account', 'is_active')
