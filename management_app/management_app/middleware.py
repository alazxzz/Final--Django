from django.conf import settings
from django.http import HttpResponseForbidden

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = ['192.168.1.1']  #заблокированные IP-адреса
        if request.META['REMOTE_ADDR'] in blocked_ips:
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)
