from django.urls import path
import django.contrib.auth.views as auth
from accounts.views import Registration
 
urlpatterns = [
    path('login/', auth.LoginView.as_view(), name = 'login'),
    path('logout/', auth.LogoutView.as_view(), name = 'logout'),
    path('register/', Registration.as_view(), name = 'register' ),
    path('password_change/', auth.PasswordChangeView.as_view(), name = "change_password"),
    path('password_change_done/', auth.PasswordChangeDoneView.as_view(), name = "password_change_done"),
    path('password_reset/', auth.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset_done/', auth.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]
