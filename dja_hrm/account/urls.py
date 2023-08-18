from django.urls import path,include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views
from .views import SignUpView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/login/')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
    # change password urls
    path('password-change/',auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
