from rest_framework import generics
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from monitoring.models import (
    FuelStation, Cars, Drivers, FuelStationRefill, CarRefill,
    Warehouse, Contactor, Autopart,
)
from .serializer import (
    CarRefillListSerializer, FuelStationListSerializer, CarsListSerializer,
    DriversListSerializer, FuelStationRefillListSerializer, AutopartListSerializer,
    ContactorListSerializer,WarehouseListSerializer, 
)
from .filters import (
    FuelStationRefillFilter, CarRefillFilter, AutopartFilter
)
# Filtered classes

class FuelStationRefillListAPIView(generics.ListAPIView):
    queryset = FuelStationRefill.objects.all()
    serializer_class = FuelStationRefillListSerializer
    filterset_class = FuelStationRefillFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)


class CarRefillListAPIView(generics.ListAPIView):
    queryset = CarRefill.objects.all()
    serializer_class = CarRefillListSerializer
    filterset_class = CarRefillFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)

class AutopartListAPIView(generics.ListAPIView):
    queryset = Autopart.objects.all()
    serializer_class = AutopartListSerializer
    filterset_class = AutopartFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = (IsAuthenticated,)

# Base classes

class DriversListAPIView(generics.ListAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversListSerializer
    permission_classes = (IsAuthenticated,)

class FuelStationListAPIView(generics.ListAPIView):
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationListSerializer
    permission_classes = (IsAuthenticated,)

class CarsListAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsListSerializer
    permission_classes = (IsAuthenticated,)

class WarehouseListAPIView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseListSerializer
    permission_classes = (IsAuthenticated,)

class ContactorListAPIView(generics.ListAPIView):
    queryset = Contactor.objects.all()
    serializer_class = ContactorListSerializer
    permission_classes = (IsAuthenticated,)



