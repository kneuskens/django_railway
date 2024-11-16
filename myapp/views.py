from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def deploy_check(request):
    return HttpResponse("<h1>Deployment unbelievable Successful!</h1><p>If you see this message, your app is working correctly.</p>")