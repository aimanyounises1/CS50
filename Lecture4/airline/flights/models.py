from django.db import models

# Create your models here. every model is python class

'''
origin = models.ForeignKey(Airport , on_delete = models.CASCADE, related_name = "departures")
    destination = models.ForeignKey(Airport , on_delete= models.CASCADE, related_name = "arrivals")
    duration = models.IntegerField()'''


class Airport(models.Model):
    code = models.CharField(max_length = 3)
    city = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.code} ({self.city})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport , on_delete = models.CASCADE , related_name ="departures") 
    destination = models.ForeignKey(Airport , on_delete = models.CASCADE , related_name ="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} time {self.duration}"



class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length =64)
    # blank is equal to true to allow that the passenger aren't registered to any flights.
    # ManytoMany relationships means that passenger can have more than one flight
    # passenger is to access all the passengers on that plane
    flights = models.ManyToManyField(Flight , blank=True ,related_name ="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"