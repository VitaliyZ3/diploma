from django.urls import path
from .views import (
    CarRefillListAPIView, FuelStationListAPIView, CarsListAPIView, DriversListAPIView,
    FuelStationRefillListAPIView, WarehouseListAPIView, ContactorListAPIView, AutopartListAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('car-refill/', CarRefillListAPIView.as_view()),
    path('fuelstation/', FuelStationListAPIView.as_view()),
    path('cars/', CarsListAPIView.as_view()),
    path('drivers/', DriversListAPIView.as_view()),
    path('fuelstation-refill/', FuelStationRefillListAPIView.as_view()),
    path('warehouse/', WarehouseListAPIView.as_view()),
    path('contactor/', ContactorListAPIView.as_view()),
    path('autopart/', AutopartListAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]