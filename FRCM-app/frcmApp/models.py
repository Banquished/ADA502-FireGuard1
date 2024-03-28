from django.db import models

# Create your models here.

class WeatherStation(models.Model):
    station_id = models.CharField(max_length=255, unique=True, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=255)
    prediction = models.FloatField()
    updated = models.DateTimeField(auto_now=True) #Saves the timestamp when data is saved
    created = models.DateTimeField(auto_now_add=True) #Only take a timestamp when the data is created
    
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.city
