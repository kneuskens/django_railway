from django.urls import path
from .views import deploy_check

urlpatterns = [
    path('', deploy_check, name='deploy_check'),
]