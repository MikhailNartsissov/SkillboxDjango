from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    AboutMeView,
    RegistrationView,
)

app_name = "myauth"

urlpatterns = [
    path("login/", LoginView.as_view
         (
             template_name='myauth/login.html',
             redirect_authenticated_user=True
            ),
         name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
]
