
from rest_framework import serializers
from vehiclerent.models import Customer, Inventory, RentBooking

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

