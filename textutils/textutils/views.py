#File Created by Paarth
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1><b>Hello Paarth</b></h1><a href='https://github.com/'>Github</a>")

def about(request):
    return HttpResponse("About Paarth Bathla")

