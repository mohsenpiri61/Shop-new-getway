from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm, SignUpForm
from django.urls import reverse_lazy
from .models import User
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView
from .tasks import send_reset_password_email
# from django.contrib.messages.views import SuccessMessageMixin



class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True



class LogoutView(auth_views.LogoutView):
    pass



class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


    # overriding form_valid for invalid email addresses
    def form_valid(self, form):
        email = form.cleaned_data.get('email')       
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, 'ایمیل وارد شده در سیستم موجود نیست.')
            return render(self.request, self.template_name, {'form': form})
        
        recipient_list = [email]
        subject = 'Reset your password'
        message = 'Click the link to reset your password'
        send_reset_password_email.delay(subject, message, recipient_list)
        return super().form_valid(form)
    
    

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'




class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/page-signup-simple.html'
    success_url = reverse_lazy('accounts:login')


    def form_valid(self, form):
        messages.success(self.request, "،The new user was created successfully")
        return super().form_valid(form)

