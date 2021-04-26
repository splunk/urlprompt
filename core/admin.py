from django.contrib import admin
from core.models import Prompt

from django.contrib import admin
from django.contrib.auth.models import User
from core.models import CustomUser
from django.contrib.auth.admin import UserAdmin

class PromptAdmin(admin.ModelAdmin):
    list_display = ['id','status', 'created_by']

admin.site.register(Prompt, PromptAdmin)

# Register out own model admin, based on the default UserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
