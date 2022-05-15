from django import views
from django.urls import path

from .views import (
    mainpage, CarRefillCreateView, FuelstationRefillCreateView, CarRefillListView, FuelStationRefillListView,
    AutopartCreateView, AutopartListView, AutopartOffUpdate, AutopartDetailView, AutopartOffListView, CarRefillDetailView
  )

urlpatterns = [
    path('', mainpage, name='mainpage'),
    # ЗАПРАВКИ
    
    path('create-car_refill/', CarRefillCreateView.as_view(), name='create-car_refill'),
    path('create-fuel_station_refill/', FuelstationRefillCreateView.as_view(), name='create-fuel_station_refill'),


    path('list-car_refill/', CarRefillListView.as_view(), name='list-car_refill'),
    path('list-fuel_station_refill/', FuelStationRefillListView.as_view(), name='list-fuel_station_refill'),
    path('list-car_refill-detail/<int:pk>', CarRefillDetailView.as_view(), name='list-car_refill-detail'),
    # АВТОЗАПЧАСТИ

    # Создание 
    path('create-autopart/', AutopartCreateView.as_view(), name='create-autopart'),

    # Просмотр деталей
    path('list-autopart/', AutopartListView.as_view(), name='list-autopart'),
    path('list-autopart-detail/<int:pk>', AutopartDetailView.as_view(), name='list-autopart-detail'),

    # Просмотр деталей которые есть на складе
    path('list-autopart_off/', AutopartOffListView.as_view(), name='list-autopart-off'),
    path('list-autopart_off_detail/<int:pk>', AutopartOffUpdate.as_view(), name='list-autopart-off-detail'),



]
