from django.shortcuts import render
from django.http import HttpResponse

home="""
<h1> Manzilar </h1><br>
<span> 127.0.0.1:8000/app1 </span><br>
<span> 127.0.0.1:8000/app1/abaut</span><br>
<span> 127.0.0.1:8000/app1/contact</span><br>
<span> 127.0.0.1:8000/app2 </span><br>
<span> 127.0.0.1:8000/app2/abaut</span><br>
<span> 127.0.0.1:8000/app2/contact</span><br>
<span> 127.0.0.1:8000/app3 </span><br>
<span> 127.0.0.1:8000/app3/abaut</span><br>
<span> 127.0.0.1:8000/app3/contact</span><br>
"""


def homepage(request):
    return HttpResponse(home)

