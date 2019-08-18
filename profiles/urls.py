from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as av

from profiles.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),

    # Login/Logout views
    path('login/', av.LoginView.as_view(template_name='users/user_login.html'),
         name='user-login'),
    path('logout/', av.LogoutView.as_view(), name='user-logout'),

    # Password reset
    path('password-change/',
            av.PasswordChangeView.as_view(template_name='users/user_password_change.html'), name='password_change'
    ),
    path('password-change/done/',
            av.PasswordChangeDoneView.as_view(template_name='users/user_password_change_done.html'),
            name='password_change_done'
    ),

    # All auth
    path('auth/', include('allauth.urls')),
]
