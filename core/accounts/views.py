from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import (
#      PasswordResetView, PasswordResetDoneView,
#      PasswordResetConfirmView, PasswordResetCompleteView,
#      PasswordChangeView, PasswordChangeDoneView, LoginView)

from accounts.forms import AuthenticationForm
from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    # success_url = '/'
    # success_message = "You have registered successfully!"

class LogoutView(auth_views.LogoutView):
    pass



class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')



class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
