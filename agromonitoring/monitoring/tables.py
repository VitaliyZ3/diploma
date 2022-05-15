from django.db import models
import django_tables2 as tables
from .models import CarRefill, FuelStationRefill, Autopart

class CarRefillTable(tables.Table):
    class Meta:
        model = CarRefill
        fields = (
            'id',
            'fuel_station',
            'cars',
            'driver',
            'fillin_volume',
            'date_of_fuel',
            'description'
        )
        template_name = "django_tables2/bootstrap.html"



class FuelStationRefillTable(tables.Table):
    class Meta:
        model = FuelStationRefill
        template_name = "django_tables2/bootstrap.html"

class AutopartTable(tables.Table):
    class Meta:
        model = Autopart
        template_name = "django_tables2/bootstrap.html"