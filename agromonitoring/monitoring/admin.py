from django.contrib import admin

from .models import FuelStation, Cars, Drivers, Contactor, Warehouse, Autopart, Status


admin.site.register(Cars)
admin.site.register(Drivers)
admin.site.register(FuelStation)

admin.site.register(Contactor)
admin.site.register(Warehouse)
admin.site.register(Autopart)
admin.site.register(Status)
