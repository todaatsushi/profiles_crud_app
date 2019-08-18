from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as av

import users.views as v


urlpatterns = [
    path('', v.AllBaseUsersView.as_view(), name='user-list'),

    # Profile paths
    path('user/new/', v.BaseUserCreateView.as_view(), name='user-create'),
    path('user/<str:slug>/', v.BaseUserDetailView.as_view(), name='user-detail'),
    path('user/<str:slug>/update/', v.BaseUserUpdateView.as_view(), name='user-update'),
    path('user/<str:slug>/delete/', v.BaseUserDeleteView.as_view(), name='user-delete'),

    # Login/Logout views
    path('user/login/', av.LoginView.as_view(template_name='users/user_login.html'), name='user-login'),
    path('user/logout/', av.LogoutView.as_view(), name='user-logout'),

    # Password reset
    path('user/password-reset/', av.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('user/password-reset/done/', av.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('user/password-reset-confirm/<uidb64>/<token>/', av.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('user/password-reset-complete', av.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
