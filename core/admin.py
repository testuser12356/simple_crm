from django.contrib import admin
import core.models as models


# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display_links = ("id", "username")
    readonly_fields = ("password", "last_login")
    list_display = ("id", "username", "is_active", "last_login")
