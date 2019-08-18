from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as av

import users.views as v


urlpatterns = [
    path('', v.AllBaseUsersView.as_view(), name='user-list'),

    # Profile paths
    path('new/', v.BaseUserCreateView.as_view(), name='user-create'),
    path('<str:slug>/', v.BaseUserDetailView.as_view(), name='user-detail'),
    path('<str:slug>/update/', v.BaseUserUpdateView.as_view(), name='user-update'),
    path('<str:slug>/delete/', v.BaseUserDeleteView.as_view(), name='user-delete'),

    # Password reset
    path('password-change/',
            av.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'
    ),
    path('password-change/done/',
            av.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
            name='password_change_done'
    ),
]
