from django.contrib import admin

# Register your models here.
from django.contrib import admin
from super_cars.models import Cars

# Register your models here.
from super_cars.models import Cars
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name')
    search_fields = ('car_name',)

admin.site.register(Cars, CarsAdmin)
