from django.urls import path
from .views.cars import CarsApi
from .views.tokens import TokensApi

urlpatterns = [
    path('cars',CarsApi.as_view()),
    path('cars/<int:pk>',CarsApi.as_view()),
    path('token',TokensApi.as_view()),
]
