"""
Views for users app
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from http import HTTPStatus
from django.views import View
# Create your views here.
from allauth.account.views import LogoutView


# class UserSignupView(SignupView):
#

# """Example to override the Login form and same can be done for the signup form """
# avoiding too-many-ancestors
# pylint: disable=R0901
# from allauth.account.views import SignupView, LoginView
# class UserLoginView(LoginView):
#     """
#     creating custom login view
#     """
#     form_class = CustomLoginForm
#
#     def get_context_data(self, **kwargs):
#         ret = super().get_context_data(**kwargs)
#         return ret


class LoggedInView(View):
    """
    Created View where user will be redirected after login
    """

    def get(self, request):
        """
        Get method will be called after user successfully logs in

        @param request: Request Object received in request
        @return: render: It is used to load the html file with the data
        """
        return render(request, "users/user.html", status=HTTPStatus.O)


class CustomLogoutView(LogoutView):
    """
    Created custom logout view to overide the post method
    """
    def post(self, *args, **kwargs):
        """
        over riding the post method in order to generate 200 response code

        @param args: receive args from the base class
        @param kwargs: receive kwargs from the base class
        @return: JSONResponse with the redirect url and status code as 200
        """
        url = self.get_redirect_url()
        if self.request.user.is_authenticated:
            self.logout()
        return JsonResponse({"url": url, "status": "OK123"})


class IndexView(View):
    """
    Defining the index view for Homepage
    """

    # pylint: disable=W0613
    def get(self, request):
        """
        Redirecting to Login page

        @return: when index api is hit we are simply redirecting to login page
        """
        return HttpResponseRedirect("/accounts/login")
