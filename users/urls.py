from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserView

urlpatterns = [
    path(
        '',
        auth_views.LoginView.as_view(
            template_name = 'userform.html'
        ),
        name = 'login'),
        path(
            'logout/',
            auth_views.LogoutView.as_view(
                template_name = 'profile.html'
            ),
            name = 'logout'),
]