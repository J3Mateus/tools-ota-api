from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.role.models import Roles

from apps.users.models import BaseUser, BaseUserRoles


class BaseUserRolesInline(admin.TabularInline):
    model = BaseUserRoles
    extra = 1


@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    inlines = [BaseUserRolesInline]

    list_display = ("email", "full_name", "is_admin", "is_superuser", "is_active", "created_at", "updated_at")
    search_fields = ("email", "full_name", "phone", "whatsapp")
    list_filter = ("is_active", "is_admin", "is_superuser")
    ordering = ("email",)  # Escolha um campo válido para ordenar, como "email" ou "created_at"
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name", "phone", "whatsapp")}),
        ("Permissions", {"fields": ("is_active", "is_admin", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone', 'whatsapp', 'password1', 'password2'),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

admin.site.register(Roles)