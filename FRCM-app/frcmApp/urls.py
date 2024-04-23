from django.urls import path, include
from rest_framework.routers import DefaultRouter
from frcmApp import views
from .views import WeatherStationViewSet


router = DefaultRouter()
router.register(r'weatherstations', WeatherStationViewSet, basename='weatherstation')

urlpatterns = [
    path('', include(router.urls)),  # This will include all URLs handled by the router
    path('api/fire-risk-prediction/', views.fire_risk_prediction, name='fire_risk_prediction'),
]