from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WeatherStation
from .serializers import WeatherStationSerializer
from frcmApp.src.main import FireRiskApplication
from django.core.exceptions import ValidationError
from rest_framework import status
import logging


logger = logging.getLogger(__name__)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/city',
        'GET /api/city/id',
        'GET /api/update/id'
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
        
        # Simplified for explanation - Extracting 'firerisks' directly and assuming it's structured as expected
        firerisks = all_predictions.get('firerisks', [])
        
        # Check if 'firerisks' is not empty and contains dictionaries with a 'timestamp' and 'ttf'
        if firerisks:
            # Assuming 'firerisks' is a list of dictionaries with 'timestamp' and 'ttf'
            most_recent_firerisk = max(firerisks, key=lambda x: x['timestamp'])
        else:
            most_recent_firerisk = {}
        
        # Include location in the response
        location_info = {
            'latitude': lat,
            'longitude': lon
        }
        
        data = {
            'location': location_info,
            'prediction': most_recent_firerisk
        }
    except Exception as e:
        logger.error('Unexpected error occurred: %s', e, exc_info=True)
        return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(data)