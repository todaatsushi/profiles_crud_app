from django.contrib import admin
from django.urls import path, include

import users.views as v


urlpatterns = [
    path('', v.AllBaseUsersView.as_view(), name='users-list'),
    path('<str:pk>/', v.BaseUserDetailView.as_view(), name='users-detail'),
]
