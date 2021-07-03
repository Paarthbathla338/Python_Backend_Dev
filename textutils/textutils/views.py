#File Created by Paarth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    param={"name":"Paarth", "place":"United States" }
    return render(request,'index.html',param)

def removepunc(request):
    return HttpResponse("About Paarth Bathla")

