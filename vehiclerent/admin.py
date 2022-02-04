from django.contrib import admin
from vehiclerent.models import Customer , Inventory, RentBooking

# Register your models here.
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(RentBooking)
