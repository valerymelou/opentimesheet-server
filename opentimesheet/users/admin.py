from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("org", "email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("org", "email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "org", "created", "is_staff")
    list_filter = ("org", "is_staff", "is_superuser", "is_active", "created", "groups")
    search_fields = ("email",)
    ordering = ("email", "created")
    date_hierarchy = "created"
