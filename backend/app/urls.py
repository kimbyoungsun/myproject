from django.urls import path
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world),  # API 엔드포인트
]
