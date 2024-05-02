from geopy.geocoders import Nominatim
from frcmApp.src.frcm.frcapi import FireRiskAPI
from frcmApp.src.frcm.weatherdata.client_met import METClient
from frcmApp.src.frcm.weatherdata.extractor_met import METExtractor
from frcmApp.src.frcm.datamodel.model import Location
from datetime import datetime
from datetime import date
from datetime import timedelta
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from frcmApp.models import WeatherData, WeatherStation




def get_city(latitude, longitude):
    geolocator = Nominatim(user_agent="sivert.hb@outlook.com")
    location = geolocator.reverse(f"{latitude},{longitude}")
    address = location.raw['address']
    city = address.get('city', '')
    return city




# # sample code illustrating how to use the Fire Risk Computation API (FRCAPI)
# if __name__ == "__main__":

#     met_extractor = METExtractor()
#     # TODO: maybe embed extractor into client
#     met_client = METClient(extractor=met_extractor)
#     frc = FireRiskAPI(client=met_client)
    
#     # #Bergen
#     # latitude=60.383
#     # longitude=5.3327

#     # #Oslo
#     # latitude = 59.920
#     # longitude = 10.761

#     # #Stavanger
#     # latitude = 58.964
#     # longitude = 5.7338

#     # Kristiansand
#     latitude = 58.156
#     longitude = 8.0115

#     location = Location(latitude=latitude, longitude=longitude)  # Bergen
#     # location = Location(latitude=59.4225, longitude=5.2480)  # Haugesund

#     # Fails
#     # location = Location(latitude=62.5780, longitude=11.3919)  # Røros
#     # location = Location(latitude=69.6492, longitude=18.9553)  # Tromsø

#     # how far into the past to fetch observations

#     obs_delta = datetime.timedelta(days=1)

#     predictions = frc.compute_now(location, obs_delta)

#     # station_id = METClient.get_nearest_station_id(location)

#     #city = get_city(latitude, longitude)
#     #print(f'City: {city}')
    

#     station_id = met_client.get_nearest_station_id(location)
#     print(f"Nearest station ID for {latitude}, {longitude}: {station_id}")


#     print(predictions)
class FireRiskApplication:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.geolocator = Nominatim(user_agent="frcmApp")
        self.met_extractor = METExtractor()
        self.met_client = METClient(extractor=self.met_extractor)
        self.frc = FireRiskAPI(client=self.met_client)
        self.location = Location(latitude=latitude, longitude=longitude)

    def get_city(self):
        location = self.geolocator.reverse(f"{self.latitude},{self.longitude}")
        address = location.raw['address']
        city = address.get('city', '')
        return city
    
    def fetch_station_id(self, location):
        # Placeholder: implement fetching station ID
        #location = Location(latitude=self.latitude, longitude=self.longitude)
        station_id = self.met_client.get_nearest_station_id(location)
        return station_id
    
    def compute_prediction(self, location, days = 1):
        # Placeholder: implement prediction computation
        #obs_delta = datetime.timedelta(days)
        obs_delta = timedelta(days)
        predictions = self.frc.compute_now(location, obs_delta)

        today = datetime.now().date()
        todays_predictions = [pred for pred in predictions.firerisks if pred.timestamp.date() == today]
        #print (predictions)
        # for pred in todays_predictions:
        #     print(pred)
        
        print(todays_predictions[18])
        # highest_prediction = max(todays_predictions, key=lambda x: x.fire_risk_value, default=None)
        # if highest_prediction:
        #     print(f"Highest prediction for today: {highest_prediction}")
        # else:
        #     print("No predictions for today.")
        return todays_predictions
    
    def get_observations(self, location):
        today = date.today()
        yesterday = today - timedelta(days=1)
        observations = self.met_client.fetch_observations(location=location, start=yesterday, end=today)
        
        # Convert the Pydantic model to a dictionary
        observations_dict = observations.dict()
        
        # Optionally, here is where you would save or further process the data
        self.save_weather_observations(observations_dict)
        
        return observations_dict

    
    
    def save_weather_observations(self, data):
        # Extract station ID and other data
        station_id = data['source'].split(":")[0]

        # Retrieve the latitude and longitude
        latitude = Decimal(str(data['location']['latitude']))
        longitude = Decimal(str(data['location']['longitude']))

        # Ensure the WeatherStation exists in the database
        station, created = WeatherStation.objects.get_or_create(
            station_id=station_id,
            defaults={
                'latitude': latitude,
                'longitude': longitude,
                'city': get_city(latitude, longitude)  # Now using actual function to get city name
            }
        )

        # Process observations data
        for observation in data['data']:
            print(f"Timestamp: {observation['timestamp']} (Type: {type(observation['timestamp'])})")  # Debug statement
            temperature = Decimal(str(observation['temperature']))
            humidity = Decimal(str(observation['humidity']))
            wind_speed = Decimal(str(observation['wind_speed']))
            #timestamp = parse_datetime(observation['timestamp'])
            timestamp = parse_datetime(str(observation['timestamp']))

            # Create and save a WeatherData instance
            WeatherData.objects.create(
                station=station,
                latitude=latitude,
                longitude=longitude,
                temperature=temperature,
                humidity=humidity,
                wind_speed=wind_speed,
                created=timestamp
            )



    
    
    
if __name__ == "__main__":
    app = FireRiskApplication()  # Example for Bergen
    


