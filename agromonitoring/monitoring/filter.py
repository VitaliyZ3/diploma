from dataclasses import field
import django_filters
from .models import Autopart, CarRefill, FuelStationRefill

class AutopartFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Autopart
        fields = '__all__'


class CarRefillFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        fields = (   
            'id',
            'fuel_station',
            'cars',
            'driver',
            'fillin_volume',
            'date_of_fuel'
        )
        model = CarRefill
        
class FuelStationRefillFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        fields = (
            'id',
            'fuel_station',
            'refill_volume',
            'date_of_refill'
        )
        
        model = FuelStationRefill
