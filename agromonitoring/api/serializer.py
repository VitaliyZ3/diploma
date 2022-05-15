from rest_framework import serializers
from monitoring.models import (
    FuelStation, Cars, Drivers, FuelStationRefill, CarRefill,
    Warehouse, Contactor, Autopart
)

class CarRefillListSerializer(serializers.ModelSerializer):
    cars = serializers.SlugRelatedField(slug_field='number', read_only=True)
    driver = serializers.SlugRelatedField(slug_field='surname', read_only=True)
    class Meta:
        model = CarRefill
        fields = '__all__'

class FuelStationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = '__all__'

class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class DriversListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'

class FuelStationRefillListSerializer(serializers.ModelSerializer):
    fuel_station = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = FuelStationRefill
        fields = '__all__'

class AutopartListSerializer(serializers.ModelSerializer):
    warehouse = serializers.SlugRelatedField(slug_field='name', read_only=True)
    contactor = serializers.SlugRelatedField(slug_field='name', read_only=True)
    status = serializers.SlugRelatedField(slug_field='status', read_only=True)
    class Meta:
        model = Autopart
        fields = '__all__'

class ContactorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactor
        fields = '__all__'

class WarehouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
