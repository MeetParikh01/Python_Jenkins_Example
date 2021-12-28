"""
    Register the users app modules to display model data in django admin panel
"""
from django.contrib import admin
from users.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Registering the user model in django admin
    """
