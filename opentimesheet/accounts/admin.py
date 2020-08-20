from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("__str__", "hire_date", "release_date", "created", "created_by")
    list_filter = ("hire_date", "created")
    search_fields = ("user__email", "first_name", "last_name")
    date_hierarchy = "created"
