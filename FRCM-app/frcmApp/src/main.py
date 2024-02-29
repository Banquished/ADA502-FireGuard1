import datetime

from geopy.geocoders import Nominatim
from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location




def get_city(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{latitude},{longitude}")
    address = location.raw['address']
    city = address.get('city', '')
    return city

# def save_station_data(station_id, latitude, longitude, city, prediction):
#     # Create a new WeatherStation instance and save it to the database
#     station, created = WeatherStation.objects.update_or_create(
#         station_id=station_id,
#         defaults={'latitude': latitude, 'longitude': longitude, 'city': city, 'prediction': prediction}
#     )
#     if created:
#         print(f"Added new station: {station}")
#     else:
#         print(f"Updated existing station: {station}")



# sample code illustrating how to use the Fire Risk Computation API (FRCAPI)
if __name__ == "__main__":

    met_extractor = METExtractor()
    # TODO: maybe embed extractor into client
    met_client = METClient(extractor=met_extractor)
    frc = FireRiskAPI(client=met_client)
    
    # #Bergen
    # latitude=60.383
    # longitude=5.3327

    # #Oslo
    # latitude = 59.920
    # longitude = 10.761

    # #Stavanger
    # latitude = 58.964
    # longitude = 5.7338

    # Kristiandsand
    latitude = 58.156
    longitude = 8.0115

    location = Location(latitude=latitude, longitude=longitude)  # Bergen
    # location = Location(latitude=59.4225, longitude=5.2480)  # Haugesund

    # Fails
    # location = Location(latitude=62.5780, longitude=11.3919)  # Røros
    # location = Location(latitude=69.6492, longitude=18.9553)  # Tromsø

    # how far into the past to fetch observations

    obs_delta = datetime.timedelta(days=1)

    predictions = frc.compute_now(location, obs_delta)

    #station_id = METClient.get_nearest_station_id(location)

    #city = get_city(latitude, longitude)
    #print(f'City: {city}')
    #print(station_id)

    station_id = met_client.get_nearest_station_id(location)
    print(f"Nearest station ID for {latitude}, {longitude}: {station_id}")


    print(predictions)

# import datetime
# from geopy.geocoders import Nominatim
# from frcm.frcapi import FireRiskAPI
# from frcm.weatherdata.client_met import METClient
# from frcm.weatherdata.extractor_met import METExtractor
# from frcm.datamodel.model import Location

# class FireRiskApplication:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.geolocator = Nominatim(user_agent="geoapiExercises")
#         self.met_extractor = METExtractor()
#         self.met_client = METClient(extractor=self.met_extractor)
#         self.frc = FireRiskAPI(client=self.met_client)
#         self.location = Location(latitude=latitude, longitude=longitude)

#     def get_city(self):
#         location = self.geolocator.reverse(f"{self.latitude},{self.longitude}")
#         address = location.raw['address']
#         city = address.get('city', '')
#         return city
    
#     def fetch_station_id(self, location):
#         # Placeholder: implement fetching station ID
#         station_id = METClient.get_nearest_station_id(location)
#         return station_id
    
#     def compute_prediction(self, location, days = 2):
#         # Placeholder: implement prediction computation
#         obs_delta = datetime.timedelta(days)
#         predictions = self.frc.compute_now(location, obs_delta)
#         return predictions
    
# if __name__ == "__main__":
#     app = FireRiskApplication(latitude=60.383, longitude=5.3327)  # Example for Bergen
    


