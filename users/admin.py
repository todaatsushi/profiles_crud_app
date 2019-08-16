from django.contrib import admin

import users.forms as forms
from users.models import BaseUser


class BaseUserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'is_staff', 'first_name', 'last_name',
        'about', 'company', 'role',
    )
    fields = [
        ('first_name', 'last_name', 'email'),
        'is_staff', 'about',
        ('company', 'role'),
        'responsibilities',
    ]


admin.site.register(BaseUser, BaseUserAdmin)
