from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WeatherStation
from .serializers import WeatherStationSerializer
from django.http import JsonResponse
from .models import Location  # Update this with the correct import path
from .frcapi import  FireRiskAPI # Update this with the correct import path
from .weatherdata.client import WeatherDataClient  # Adjust the import as neede

class WeatherStationViewSet(viewsets.ModelViewSet):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer

    @action(detail=False, methods=['get'])
    def predictionset(self, request):
        queryset = WeatherStation.objects.all()
        serializer = WeatherStationSerializer(queryset, many=True)
        return Response({'prediction': serializer.data})
    
    def fire_risk_prediction(request):
    # You can use GET parameters or path variables to specify the location
        location_id = request.GET.get('location_id')
    
    # Fetch the location details from your database or parse the request data
        location = Location.objects.get(id=location_id)
    
    # Initialize your WeatherDataClient and FireRiskAPI
        weather_client = WeatherDataClient()
        fire_risk_api = FireRiskAPI(client=weather_client)
    
    # Perform the calculation (the parameters will depend on your specific implementation)
        prediction = fire_risk_api.compute_now(location, datetime.timedelta(hours=1))  # Example timedelta
    
    # Convert the prediction to a dictionary and return as JSON
        return JsonResponse(prediction.to_dict(), safe=False)