from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WeatherStation
from .serializers import WeatherStationSerializer

class WeatherStationViewSet(viewsets.ModelViewSet):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer

    @action(detail=False, methods=['get'])
    def predictionset(self, request):
        queryset = WeatherStation.objects.all()
        serializer = WeatherStationSerializer(queryset, many=True)
        return Response({'prediction': serializer.data})