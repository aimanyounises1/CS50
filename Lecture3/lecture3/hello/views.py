from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates/index.html')

def aiman(request):
    return HttpResponse("Hello , Aiman")


def greet(request , name):
    return render(request, 'greet.html',{
        'name': name.capitalize()
    })