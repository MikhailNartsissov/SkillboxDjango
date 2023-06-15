from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import CreateView, FormView, View, ListView, DetailView

from .models import Profile
from .forms import AvatarForm


class AboutMeView(PermissionRequiredMixin, FormView):
    permission_required = ["myauth.view_profile"]
    template_name = "myauth/about-me.html"
    form_class = AvatarForm
    success_url = "."

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        form = AvatarForm(self.request.POST or None)
        context['avatar_form'] = form
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        image = form.files.get("avatar")
        user = self.request.user
        if Profile.objects.filter(user=user):
            user.profile.avatar = image
            user.profile.save()
        else:
            Profile.objects.create(
                user=user,
                avatar=image,
            )
        return response


class UsersListView(ListView):
    template_name = 'myauth/users_list.html'
    queryset = User.objects.all()
    context_object_name = "users"


class UserDetailsView(PermissionRequiredMixin, DetailView):
    permission_required = ["myauth.view_profile"]
    template_name = 'myauth/user-details.html'
    model = User
    context_object_name = 'user'
    form_class = AvatarForm
    success_url = "."

    def get_context_data(self, **kwargs):
        context = super(UserDetailsView, self).get_context_data(**kwargs)
        context['avatar_form'] = AvatarForm()
        return context

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        user = self.get_object()
        image = request.FILES["avatar"]
        if Profile.objects.filter(user=user):
            user.profile.avatar = image
            user.profile.save()
        else:
            Profile.objects.create(
                user=user,
                avatar=image,
            )
        return redirect(request.path)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})
