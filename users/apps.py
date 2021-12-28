"""
Django configuration for the user app file
"""

from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Configuration for users django app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
