from django.contrib import admin
from django.urls import path, include

import users.views as v


urlpatterns = [
    path('', v.AllBaseUsersView.as_view(), name='user-list'),
    path('user/new/', v.BaseUserCreateView.as_view(), name='user-create'),
    path('user/<str:pk>/', v.BaseUserDetailView.as_view(), name='user-detail'),
    path('user/<str:pk>/update/', v.BaseUserUpdateView.as_view(), name='user-update'),
]
