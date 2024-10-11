from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    # path('',include('django.contrib.auth.urls'))
    path('login/', views.LoginView.as_view(),name="login"),
    path('logout/', views.LogoutView.as_view(),name="logout"),
    # path('register/',views.RegisterView.as_view(),name="register"),
    
    # نمایش فرم وارد کردن ایمیل برای بازیابی رمز عبور
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='password_reset'),

    # # پیام موفقیت پس از ارسال ایمیل بازیابی
    path('password_reset_done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),

    # لینک بازیابی رمز عبور که به ایمیل کاربر ارسال می‌شود
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # پیام موفقیت پس از تغییر رمز عبور
    path('reset_password_complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
]