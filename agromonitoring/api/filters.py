from cgitb import lookup
from django_filters import rest_framework as filters
from monitoring.models import (
    FuelStationRefill, CarRefill, Autopart
)

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class FuelStationRefillFilter(filters.FilterSet):
    id = filters.CharFilter()
    fuel_station = filters.CharFilter(field_name = 'fuel_station__name', lookup_expr='iexact')
    refill_volume = filters.RangeFilter()
    date_min = filters.DateTimeFilter(field_name="date_of_refill", lookup_expr='gte')
    date_max = filters.DateTimeFilter(field_name="date_of_refill", lookup_expr='lte')

    class Meta:
        model = FuelStationRefill
        fields = '__all__'
    
class CarRefillFilter(filters.FilterSet):
    id = filters.CharFilter()
    fuel_station = filters.CharFilter(field_name='fuel_station__name', lookup_expr='iexact')
    cars = filters.CharFilter(field_name='cars__number', lookup_expr='iexact')
    driver = filters.CharFilter(field_name='driver__surname', lookup_expr='iexact')
    fillin_volume = filters.RangeFilter()
    date_min = filters.DateTimeFilter(field_name="date_of_fuel", lookup_expr='gte')
    date_max = filters.DateTimeFilter(field_name="date_of_fuel", lookup_expr='lte')

    class Meta:
        model = CarRefill
        fields = '__all__'

class AutopartFilter(filters.FilterSet):
    id = filters.CharFilter()
    name = filters.CharFilter()
    invent_number = filters.CharFilter()
    warehouse = filters.CharFilter(field_name='warehouse__name', lookup_expr='iexact')
    number = filters.CharFilter()
    price = filters.CharFilter()
    car_for_using = filters.CharFilter()
    contactor = filters.CharFilter(field_name='contactor__surname', lookup_expr='iexact')
    status = filters.CharFilter(field_name='status__status', lookup_expr='iexact')
    date_min = filters.DateTimeFilter(field_name="date_of_supply", lookup_expr='gte')
    date_max = filters.DateTimeFilter(field_name="date_of_supply", lookup_expr='lte')

    class Meta:
        model = Autopart
        fields = '__all__'