from django.http import HttpResponse
from django.shortcuts import render
import datetime
now = datetime.datetime.now()
# Create your views here.
def index(request): # 
    return render(request, '/home/aimnayounis/CS50/CS50/Lecture3/lecture3/newyear/templates/index.html' , {
            "newyear" : now.month==1 and now.day==1
        })
