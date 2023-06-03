from django.http import HttpRequest, HttpResponse
from django.utils.timezone import localtime
from django.shortcuts import render
from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class SuspiciousRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.session = SessionStore()

    def __call__(self, request: HttpRequest) -> HttpResponse:
        req_time = localtime().timestamp()
        key = self.session.session_key

        if key:
            if self.session[key][1] > 5 and req_time - self.session[key][0] <= 60:
                return HttpResponse("<h1>Извините, от вас поступает слишком много запросов</h1>"
                                    "<h2>К сожалению нам пришлось вас временно заблокировать.</h2>"
                                    "<h2>Подождите одну минуту и повторите запрос.</h2>")
            elif req_time - self.session[key][0] > 60:
                self.session[key][1] = 1
            else:
                self.session[key][1] += 1
            self.session[key][0] = req_time
        else:
            self.session.create()
            key = self.session.session_key
            self.session[key] = [req_time, 1]

        response = self.get_response(request)
        return response
