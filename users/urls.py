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
    path('login/', av.LoginView.as_view(template_name='users/user_login.html'),
         name='user-login'),
    path('logout/', av.LogoutView.as_view(), name='user-logout'),

    # Password reset
    path('user/password-change/',
            av.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'
    ),
    path('user/password-change/done/',
            av.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
            name='password_change_done'
    ),
]
