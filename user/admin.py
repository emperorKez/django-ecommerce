from django.contrib import admin
from user.models import User
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    search_fields = ['email']
    list_display = ['firstname', 'lastname', 'phone_number', 'is_vendor', 'date_joined']
    list_editable = ['is_vendor']
    list_filter = ['is_vendor', 'is_staff', 'country']

admin.site.register(User, UserAdmin)
