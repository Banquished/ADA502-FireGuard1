import abc

from frcmApp.src.frcm.datamodel.model import *


class WeatherDataClient:

    # TODO: add variants for time period on observations and timedelta on forecast

    @abc.abstractmethod
    def fetch_observations(self, location: Location) -> Observations:
        pass

    @abc.abstractmethod
    def fetch_forecast(self, location: Location) -> Forecast:
        pass

    # @abc.abstractmethod
    # def get_nearest_station_id(self, location: Location) -> Station_id:
    #     pass
