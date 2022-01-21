"""
creating form classes for users app
"""
from django import forms
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.helper import FormHelper
from allauth.account.forms import SignupForm, LoginForm


class CustomLoginForm(LoginForm):
    """
    Created Custom login form to be used instead of default allauth login form
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        login_widget = forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": "E-mail address",
                "autocomplete": "email",
                "class": "input100",
                "id": "email"
            }
        )
        login_field = forms.EmailField(label="E-mail", widget=login_widget)
        self.fields.update({"login": login_field})

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "placeholder": 'Password',
        "id": "password",
        "class": "input100",
        "data-name": "mhp"
    }))
