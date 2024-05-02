from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WeatherStation, WeatherData
from .serializers import WeatherStationSerializer, WeatherDataSerializer
from frcmApp.src.main import FireRiskApplication
from django.core.exceptions import ValidationError
from rest_framework import status
import logging
from frcmApp.src.frcm.weatherdata.client_met import METClient
from frcmApp.src.frcm.datamodel.model import Location
from django.shortcuts import get_object_or_404



logger = logging.getLogger(__name__)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/city',
        'GET /api/city/<str:pk>/',
        'GET /api/prediction/<str:lat>/<str:lon>/',
        'GET /api/station/<str:station_id>/',
        'GET /api/getdata/<str:city>/',
        'GET /api/weather/<str:lat>/<str:lon>/',
    ]
    
    return Response(routes)

@api_view(['GET'])
def getPredictionAll(request):
    queryset = WeatherStation.objects.all()
    serializer = WeatherStationSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPredictioCity(request, pk):
    queryset = WeatherStation.objects.get(id=pk)
    serializer = WeatherStationSerializer(queryset, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# def updateData(request, lat, long):
#     app = FireRiskApplication(latitude=lat, longitude=long)
#     city = app.get_city()
#     predictions = app.compute_prediction(app.location, days=1)
#     data = {
#         'city': city,
#         'predictions': predictions
#     }
#     return Response(data)

# @api_view(['GET'])
# def updateData(request, lat, lon):
#     try:
#         lat = float(lat)
#         lon = float(lon)
#     except ValueError as e:
#         return Response({'error': 'Invalid latitude or longitude values.'}, status=status.HTTP_400_BAD_REQUEST)
    
#     try:
#         app = FireRiskApplication(latitude=lat, longitude=lon)
#         #city = app.get_city()
#         predictions = app.compute_prediction(app.location, days=1)
#     except Exception as e:
#         # Log the exception
#         logger.error('Unexpected error occurred: %s', e, exc_info=True)
#         return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#     data = {
#         #'city': city,
#         'predictions': predictions
#     }
#     return Response(data)

@api_view(['GET'])
def updateData(request, lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError as e:
        return Response({'error': 'Invalid latitude or longitude values.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        app = FireRiskApplication(latitude=lat, longitude=lon)
        all_predictions = app.compute_prediction(app.location, days=1)
        #location = Location(latitude=lat, longitude=lon)
        # Simplified for explanation - Extracting 'firerisks' directly and assuming it's structured as expected
        #firerisks = all_predictions.get('firerisks', [])
        data = all_predictions[18]
        fire_risk_value = data.ttf
        print(fire_risk_value)
        city = app.get_city()
        station_id = app.fetch_station_id(app.location)

        print(type(lat))
        station, created = WeatherStation.objects.update_or_create(
                station_id=station_id,
                defaults={
                    'latitude': (lat),
                    'longitude': (lon),
                    'city': city,
                    'prediction': fire_risk_value
                }
            )
        result = {
                'city': city,
                'station': station_id,
                'prediction': data
                
            }
    except Exception as e:
        logger.error('Unexpected error occurred: %s', e, exc_info=True)
        return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(result, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_prediction_data(request, lat, lon):
    try:
        app = FireRiskApplication(latitude= lat, longitude=lon)
        prediction = app.compute_prediction(app.location)
    except ValueError as e:
        return Response({'error': 'Invalid latitude or longitude values.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(prediction)

@api_view(['GET'])
def get_weather_data(request, lat, lon):
    try:
        app = FireRiskApplication(latitude= lat, longitude=lon)
        data = app.get_observations(location=app.location)
    except ValueError as e:
        return Response({'error': 'Invalid latitude or longitude values.'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(data)

@api_view(['GET'])
def get_data_city(request, city):
    # Fetch the weather station by city or return 404 if not found
    queryset = get_object_or_404(WeatherStation, city__iexact=city)
    serializer = WeatherStationSerializer(queryset)
    return Response(serializer.data)

@api_view(['GET'])
def get_weather_data_by_station(request, station_id):
    """
    Retrieve weather data for a specific weather station by its ID.
    """
    try:
        weather_data = WeatherData.objects.filter(station__station_id=station_id)
        serializer = WeatherDataSerializer(weather_data, many=True)
        if weather_data.exists():
            return Response(serializer.data)
        else:
            return Response({'error': 'Weather data not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)