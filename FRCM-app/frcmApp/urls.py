from django.urls import path, include
from frcmApp import views


urlpatterns = [
    path('', views.getRoutes),
    path('city/', views.getPredictionAll),
    path('city/<str:pk>/', views.getPredictioCity),
    path('update/<str:lat>/<str:lon>/', views.updateData),
    path('prediction/<str:lat>/<str:lon>/', views.get_prediction_data),
    path('weather/<str:lat>/<str:lon>/', views.get_weather_data),
    path('getdata/<str:city>/', views.get_data_city, name='get-data-by-city'),
]