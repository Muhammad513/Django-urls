from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1 align='center'>Home Page</h2><br> <h2 align='center'>app2 ning bosh sahifasi</h2><br><hr> <h3 align='center'> 127.0.0.1:8000/app2</h3><hr>")


def abaut(request):
    return HttpResponse("<h1 align='center'>Abaut Page</h2><br> <h2 align='center'>app2 ning Abaut sahifasi</h2><br><hr> <h3 align='center'> 127.0.0.1:8000/app2/abaut</h3><hr>")


def contact(request):
    return HttpResponse("<h1 align='center'>Contact Page</h2><br> <h2 align='center'>app2 ning Contact sahifasi</h2><br><hr> <h3 align='center'> 127.0.0.1:8000/app2/contact</h3><hr>")