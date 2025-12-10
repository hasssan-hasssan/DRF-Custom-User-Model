from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):

    model = CustomUser

    list_display = ('email', 'full_name', 'is_staff',
                    'is_verified', 'is_active')
    list_filter = ('is_staff', 'is_verified', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active',
         'is_verified', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified')}
         ),
    )

    search_fields = ('email', 'full_name')
    ordering = ('email',)
