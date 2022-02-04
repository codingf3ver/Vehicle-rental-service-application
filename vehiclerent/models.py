from django.db import models


# Customer table to store the cutomer information
class Customer(models.Model):
    CustomerName_id= models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=50 )
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.CustomerName

# Vehicles inventory table to add and update stocks
class Inventory(models.Model):
    VehicleId = models.AutoField(primary_key=True)
    VehicleName = models.CharField(max_length=50)
    VehicleType = models.CharField(max_length=50)
    VehicleBrand = models.CharField(max_length=50)
    VehicleColor = models.CharField(max_length=50)
    VehicleModel = models.CharField(max_length=50)
    VehiclePrice = models.IntegerField()
    VehicleStatus = models.BooleanField(default=True)
    VehicleInventory = models.IntegerField()

    def __str__(self):
        return self.VehicleName

#  Rent booking table for registered customer by combining 
# both customer and inventory table
class RentBooking(models.Model):
    BookingId = models.AutoField(primary_key=True)
    VehicleType = models.CharField(max_length=50)
    CustomerName = models.CharField(max_length=50)
    RentDate = models.DateField()
    ReturnDate = models.DateField(default=None)
    
    
    def __str__(self):
        return f'Booked by {self.CustomerName} for {self.VehicleType}'



