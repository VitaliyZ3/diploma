
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse

# own import
from .models import CarRefill, FuelStationRefill, Autopart, FuelStation
from .tables import CarRefillTable, FuelStationRefillTable, AutopartTable
from .filter import AutopartFilter, CarRefillFilter, FuelStationRefillFilter 
# downloading fraemworks
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from django_filters import filterset

def mainpage(request):
    
    return render(request, 'monitoring/main.html')

# ЗАПРАВКИ

# Заправки транспорта
class CarRefillCreateView(generic.CreateView):
    model = CarRefill
    fields = '__all__'
    success_url = '/'

class CarRefillListView(SingleTableMixin, FilterView):
    model = CarRefill
    table_class = CarRefillTable
    template_name = 'monitoring/table_list.html'

    filterset_class = CarRefillFilter

class CarRefillDetailView(DetailView):
    model = CarRefill
    template_name = 'monitoring/carrefill_detail.html'

# Заправки станций
class FuelstationRefillCreateView(generic.CreateView):
    model = FuelStationRefill
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        refil = form.save()
        FuelStation.objects.filter(name = refil.fuel_station.name).update(total_fuel = str(FuelStation.objects.get(name = refil.fuel_station.name).total_fuel  + refil.refill_volume))
        return super().form_valid(form)
    

class FuelStationRefillListView(SingleTableMixin, FilterView):
    model = FuelStationRefill
    table_class = FuelStationRefillTable
    template_name = 'monitoring/table_list.html'

    filterset_class = FuelStationRefillFilter




# АВТОЗАПЧАСТИ

class AutopartCreateView(generic.CreateView):
   
    model = Autopart
    fields = ['name', 'invent_number', 'warehouse', 'number', 'price', 'car_for_using', 'contactor', 'description']
    success_url = '/'


class AutopartListView(SingleTableMixin, FilterView):
    model = Autopart
    table_class = AutopartTable
    template_name = 'monitoring/table_list.html'

    filterset_class = AutopartFilter

class AutopartOffListView(generic.ListView):
    
    model = Autopart
    template_name = 'monitoring/autopartoff_list.html'
    paginate_by = 5  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AutopartDetailView(DetailView):

    model = Autopart
    template_name = 'monitoring/autopart_detail.html'

class AutopartOffUpdate(UpdateView):
    
    model = Autopart
    fields = ['status']

    def get_success_url(self):
        return reverse_lazy('list-autopart-off')