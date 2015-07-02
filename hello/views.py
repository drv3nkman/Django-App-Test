from django import http

def home(request):
    return http.HttpResponse('Hello World!')

def admin(request):
		return http.HttpResponse('/admin/')