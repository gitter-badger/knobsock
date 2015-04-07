
from django import http

def home(request):
    return http.HttpResponse('KnobSock in this bish')
