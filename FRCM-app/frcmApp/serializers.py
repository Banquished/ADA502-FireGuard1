from rest_framework import serializers
from .models import WeatherStation

class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = '__all__'  # This includes all model fields in the serializer
        #May want to change fields to only include predictions and city
