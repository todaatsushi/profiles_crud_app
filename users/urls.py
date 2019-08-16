from django.contrib import admin
from django.urls import path, include

import users.views as v


urlpatterns = [
    path('', v.AllUsersView.as_view(), name='users-list'),
    path('<str:pk>/', v.UserDetailView.as_view(), name='users-detail'),
]
