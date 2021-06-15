from django.urls import path
from .views import*

urlpatterns=[
    path('',home),
    path('abaut/',abaut),
    path('contact/',contact)
]