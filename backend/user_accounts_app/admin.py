from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .model_custom_user import Gondor_mgmt

# fields = list(UserAdmin.fieldsets)
# fields[0] = (None, {'fields': ('username', 'password', 'is_bot_flag')})
# UserAdmin.fieldsets = tuple(fields)

# admin.site.register(Gondor_mgmt, UserAdmin)