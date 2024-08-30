from django.contrib import admin
from .models import Vehicle, Service

#voy a crear las clases para ver Vehicle y Service desde el admin

	list_display = (
class VehicleAdmin(admin.ModelAdmin):
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
		'car_mechanic',
    )
	

	list_display = (
admin.site.register(Vehicle, VehicleAdmin)
class ServiceAdmin(admin.ModelAdmin):
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
