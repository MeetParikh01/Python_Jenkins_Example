"""
 Creating routes for users app
"""
from django.urls import path, include
from users.views import (
    LoggedInView
)

urlpatterns = [
    path("user/", LoggedInView.as_view(), name="logged_in")
]
