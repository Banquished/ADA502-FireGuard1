import datetime

from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location, FireRiskData


# sample code illustrating how to use the Fire Risk Computation API (FRCAPI)
if __name__ == "__main__":

    met_extractor = METExtractor()

    # TODO: maybe embed extractor into client
    met_client = METClient(extractor=met_extractor)

    frc = FireRiskAPI(client=met_client)

    # location = Location(latitude=60.383, longitude=5.3327)  # Bergen
    # # location = Location(latitude=59.4225, longitude=5.2480)  # Haugesund

    # # Fails
    # # location = Location(latitude=62.5780, longitude=11.3919)  # Røros
    # # location = Location(latitude=69.6492, longitude=18.9553)  # Tromsø

    locations = [
        Location(latitude=60.3913, longitude=5.3221),  # Bergen
        #Location(latitude=58.969975, longitude=5.733107),  # Stavanger
        #Location(latitude=59.9139, longitude=10.7522),  # Oslo
        #Location(latitude=58.14671, longitude=7.9956),  # Kristiansand
    ]

    # how far into the past to fetch observations

    obs_delta = datetime.timedelta(days=2)

    # predictions = frc.compute_now(location, obs_delta)

    # print(predictions)
    for location in locations:
        predictions = frc.compute_now(location, obs_delta)
        print(f"Predictions for {location}:")
        print(predictions)


    # ## For saving to db:
    # for location in locations:
    #     predictions = frc.compute_now(location, obs_delta)
    #     print(f"Predictions for {location}:")
    #     print(predictions)
        
    #     fire_risk_data = FireRiskData(
    #         location_name="Location Name",  
    #         temperature=predictions['temperature'],
    #         humidity=predictions['humidity'],
    #         wind_speed=predictions['wind_speed'],
    #         timestamp=predictions['timestamp'],
    #     )
    #     fire_risk_data.save()
