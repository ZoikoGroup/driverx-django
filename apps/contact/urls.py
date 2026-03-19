from django.urls import path
from .views import ContactMessageAPI

urlpatterns = [
    path('contact/', ContactMessageAPI.as_view(), name='contact'),
]