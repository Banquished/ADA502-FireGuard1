from django.db import models

# Create your models here.

class WeatherStation(models.Model):
    station_id = models.CharField(max_length=255, unique=True, primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=255)
    prediction = models.FloatField()  # or another appropriate field type depending on your prediction data

    def __str__(self):
        return f"{self.city} Station"

    @property
    def lat_lon(self):
        return f"{self.latitude}, {self.longitude}"
