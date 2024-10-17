from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Engineer

admin.site.register(User, UserAdmin)
admin.site.register(Engineer)