from django.shortcuts import render
from django.http import HttpResponse
from django.middleware.csrf import get_token
import json

# Create your views here.
def login_view(request):
    return render(request, "index.html")

def get_data(request):
    if request.method == "GET":
        request.META["CSRF_COOKIE_USED"] = True
        result = {"Succeed":True, "Data":get_token(request)}
        ua = request.META.get('HTTP_USER_AGENT', 'unknown')
        return HttpResponse(ua)
    elif request.method == "POST":
        content = request.POST.get("content")
        return HttpResponse(content)

def get_csrf_token(request):
    result = {"Succeed":True, "Data":get_token(request)}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")