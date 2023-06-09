from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    AboutMeView,
    RegistrationView,
    UserUpdateView,
    UserDeleteView,
    UserPasswordChangeView,
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
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("inactive/<int:pk>/", UserDeleteView.as_view(), name="user-inactive"),
    path("<int:pk>/password/", UserPasswordChangeView.as_view(), name="password-change"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
]
