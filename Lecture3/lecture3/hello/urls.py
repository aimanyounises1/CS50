from django.urls import path
from . import views
urlpatterns =[
    path("" , views.index, name= "index"),
    path("aiman",views.aiman, name="aiman"),
    path("<str:name>" , views.greet ,name= "greet") # will pass the name as a parameter
]