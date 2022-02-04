from django.contrib import admin
from vehiclerent.models import Customer , Inventory, RentBooking

# Registering models to access from the django administration
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(RentBooking)
