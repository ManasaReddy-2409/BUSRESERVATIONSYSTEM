

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # ... other URL patterns ...

    # Login view
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # Logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ... other authentication views ...
]
