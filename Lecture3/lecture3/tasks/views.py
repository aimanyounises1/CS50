from django.shortcuts import render , HttpResponseRedirect, HttpResponse
from django import forms 
from django.urls import reverse
# a class that reperesent forms
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority  = forms.IntegerField(label= "Priority" , min_value = 1 , max_value = 10)
    age = forms.IntegerField(label= "Age")

tasks =[]
# Create your views here.
def index(request):
    if "tasks" not in request.sessions:
        request.session["tasks"] = []

    return render(request,"tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
                return render (request,"tasks/add.html",{
                    "form": form
                })
    return render(request,"tasks/add.html", {
        "form" : NewTaskForm()
    })