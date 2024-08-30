from django.contrib import admin
from autocare.forms import VehicleForm
from .models import Vehicle, Service

#voy a crear las clases para ver Vehicle y Service desde el admin

class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm
    list_display = (
        'created_at',
        'owner',
        'plate',
        'brand',
        'moddel',
        'year',
        'color',
        'car_mechanic',
    )
    search_fields = (
        'created_at',
        'plate',
        'car_mechanic__username',
    )


admin.site.register(Vehicle, VehicleAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle',
        'date',
        'kilometers',
        'service_type',
        'coments',
        'cost',
    )
    search_fields = (
        'vehicle',
        'date',
        'service_type',
    )


admin.site.register(Service, ServiceAdmin)
