from django.urls import path, include
from frcmApp import views


urlpatterns = [
    path('', views.getRoutes),
    path('city/', views.getPredictionAll),
    path('city/<str:pk>/', views.getPredictioCity),
    path('update/<str:lat>/<str:lon>/', views.updateData),
]