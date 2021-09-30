from django.contrib import admin
from core.models import Prompt
from django.urls import path

from django.contrib import admin
from django.contrib.auth.models import User
from core.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html

class PromptAdmin(SimpleHistoryAdmin):
    list_display = ['id','status', 'created_by', 'web_view']

    def web_view(self, obj):
        url = f"/?id={obj.id}"
        return format_html(f"<a href='{url}'>View</a>")


admin.site.register(Prompt, PromptAdmin)

# Register out own model admin, based on the default UserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
