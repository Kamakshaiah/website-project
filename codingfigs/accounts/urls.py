from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views 

urlpatterns = [
    path('register/', views.user_registration, name = 'register'),
    path('user_profile/<int:id>', views.UserProfile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), {'message': 'Login attempt is successful!'}, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]
