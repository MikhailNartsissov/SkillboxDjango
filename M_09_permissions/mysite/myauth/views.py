from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate, logout

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegistrationView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'myauth/registration.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            email=email,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'myauth/user_update_form.html'
    success_url = reverse_lazy('myauth:about-me')
    template_name_suffix = "_update_form"


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('myauth:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.is_active = False
        self.object.save()
        logout(self.request)
        return response


class UserPasswordChangeView(PasswordChangeView):
    model = User
    template_name = "myauth/password_change.html"
    success_url = reverse_lazy('myauth:about-me')
