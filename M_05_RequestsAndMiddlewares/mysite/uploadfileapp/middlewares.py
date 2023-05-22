from django.http import HttpRequest, HttpResponse
from django.utils.timezone import localtime
from django.shortcuts import render


class SuspiciousRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ips = {}

    def __call__(self, request: HttpRequest) -> HttpResponse:
        addr = request.META.get('REMOTE_ADDR')
        req_time = localtime().timestamp()
        if addr in self.ips.keys():
            print(self.ips[addr])
            if self.ips[addr][1] > 5 and req_time - self.ips[addr][0] <= 60:
                return render(request, "uploadfileapp/request-denial.html")
            elif req_time - self.ips[addr][0] > 60:
                self.ips[addr][0] = req_time
                self.ips[addr][1] = 1
            else:
                self.ips[addr][0] = req_time
                self.ips[addr][1] += 1
        else:
            self.ips[addr] = [req_time, 1]
        response = self.get_response(request)
        return response
