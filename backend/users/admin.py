from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from users.models import User
from django.contrib import admin


@register(User)
class UserAdmin(UserAdmin):
    def change_password_link(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.id])
        return format_html('<a href="{}">Change password</a>', url)

    change_password_link.short_description = 'Change password'
    list_display = (
        'is_active', 'username', 'first_name', 'last_name', 'email',
    )
    fields = (
        ('is_active', ),
        ('username', 'email', ),
        ('first_name', 'last_name', ),
    )
    fieldsets = []

    search_fields = (
        'username', 'email',
    )
    list_filter = (
        'is_active', 'first_name', 'email',
    )
    save_on_top = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
