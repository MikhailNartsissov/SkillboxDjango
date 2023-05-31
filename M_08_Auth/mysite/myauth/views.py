from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookies were successfully set")
    response.set_cookie("user",
                        request.META['USER'],
                        max_age=1800,
                        httponly=True,
                        )
    response.set_cookie("userIP",
                        request.META['REMOTE_ADDR'],
                        max_age=1800,
                        httponly=True,
                        )
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    user = request.COOKIES.get("user", "no user")
    user_ip = request.COOKIES.get("userIP", "no IP")
    return HttpResponse(f"<h2>Cookies set by set_cookie_view function:</h2>"
                        f"Username = {user!r}<br>User IP = {user_ip}")


def set_session_view(request: HttpRequest) -> HttpResponse:
    key = "homework_status"
    value = "completed"
    request.session[key] = value
    return HttpResponse(f"<h1>Session key = {key} successfully set to {value!r}</h1>")


def get_session_view(request: HttpRequest) -> HttpResponse:
    key = "homework_status"
    value = request.session.get(key, "unknown")
    return HttpResponse(f"<h1>Session Homework Status</h1>{key} is {value!r} now.")
