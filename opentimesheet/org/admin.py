from django.contrib import admin

from opentimesheet.org.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "website", "created", "modified")
    list_filter = ("created", "is_active")
    date_hierarchy = "created"
