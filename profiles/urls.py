from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as av

from profiles.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),

    # All auth
    path('auth/', include('allauth.urls')),
]
