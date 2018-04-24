from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('', include('tournament.urls')),

    # Django Admin
    path('admin/', admin.site.urls),

    # User management
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    # place it at whatever base url you like
]