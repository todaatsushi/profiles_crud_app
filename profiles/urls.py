from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),

    # All auth
    path('auth/', include('allauth.urls')),
]
