from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as av

import users.views as v


urlpatterns = [
    path('', v.AllBaseUsersView.as_view(), name='user-list'),

    # Login/Logout views
    path('user/login/', av.LoginView.as_view(template_name='users/user_login.html'), name='user-login'),
    path('user/logout/', av.LogoutView.as_view(), name='user-logout'),

    path('user/new/', v.BaseUserCreateView.as_view(), name='user-create'),
    path('user/<str:pk>/', v.BaseUserDetailView.as_view(), name='user-detail'),
    path('user/<str:pk>/update/', v.BaseUserUpdateView.as_view(), name='user-update'),
    path('user/<str:pk>/delete/', v.BaseUserDeleteView.as_view(), name='user-delete'),
]
