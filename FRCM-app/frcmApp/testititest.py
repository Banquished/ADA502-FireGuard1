# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FRCM.settings')  # Adjust 'FRCM-app.settings' as needed
# django.setup()

# import os
# import django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'FRCM.settings'
# django.setup()
import sys 
sys.path.insert(0, "src")
sys.path.insert(0, "../src/FRCM/")


print(sys.path)

from frcm.frcapi import FireRiskAPI
import settings

from src.main import get_city

import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FRCM.settings")

settings.co

import django
django.setup()

from django.core.management import call_command

import datetime
from models import WeatherStation
from main import FireRiskApplication


class Runner:
    @staticmethod
    def run_application(latitude, longitude):
        app = FireRiskApplication(latitude, longitude)
        city = app.get_city()
        station_id = app.fetch_station_id()
        prediction = app.compute_prediction()

        Runner.save_station_data(station_id, latitude, longitude, city, prediction)

    @staticmethod
    def save_station_data(station_id, latitude, longitude, city, prediction):
        station, created = WeatherStation.objects.update_or_create(
            station_id=station_id,
            defaults={
                'latitude': latitude,
                'longitude': longitude,
                'city': city,
                'prediction': prediction
            }
        )
        action = "Added new" if created else "Updated existing"
        print(f"{action} station: {station}")

if __name__ == "__main__":
    Runner.run_application(60.383, 5.3327)  # Example for Bergen