from django.contrib import admin
from .models import Flight , Airport
# Register your models here. 
# It will tell django that we would to be able to manipulate airport and flights 
admin.site.register(Airport)
admin.site.register(Flight)
