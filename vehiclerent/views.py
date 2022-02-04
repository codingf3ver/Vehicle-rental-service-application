from django.shortcuts import render , redirect
from django.http import HttpResponse
from vehiclerent.models import Customer ,Inventory, RentBooking
from django.contrib import messages



def home(request):
    return render(request, 'base.html')

# getting customer information from form as well as storing into database
def customerCreate(request):
    
    if request.method == 'POST':
        CustomerName = request.POST['CustomerName']        
        PhoneNumber = request.POST['PhoneNumber']
        Email = request.POST['Email']
        Address = request.POST['Address']
        Customer.objects.create(CustomerName=CustomerName, PhoneNumber=PhoneNumber, Email=Email, Address=Address)
        messages.success(request, 'Congratulations! customer has successfully been added.')
          
    return render(request, 'customerCreate.html')

# Booking request from users
def rentBookingCreate(request):

    if request.method == 'POST':

        # form data from user
        CustomerName = request.POST['CustomerName']
        VehicleType = request.POST['VehicleType']
        RentDate = request.POST['RentDate']
        ReturnDate = request.POST['ReturnDate']
        
        # check if customer exists
        customer = Customer.objects.filter(CustomerName= CustomerName).values()
        if len(customer) == 0:
            messages.error(request, f'{CustomerName} does not exist! Please register first.')
            return render(request, 'rentBookingCreate.html')
        
        # Date validation
        if (ReturnDate < RentDate):
            messages.error(request, f'Return date cannot be before rent date!')
            return render(request, 'rentBookingCreate.html')

        # Vehicle inventory check from database
        vehicleInventory = Inventory.objects.get(VehicleType=VehicleType)
        if vehicleInventory.VehicleInventory>0:
            vehicleInventory.VehicleInventory -= 1
            vehicleInventory.save()
            # storing the updated value of inventory 
            RentBooking.objects.create( CustomerName=CustomerName, VehicleType=VehicleType, RentDate=RentDate, ReturnDate=ReturnDate) 
            # sucess message for vehicle inventory
            messages.success(request, 'Congratulations! Rent booking has successfully been created.')
        
        # if inventory is out of stock         
        if  vehicleInventory.VehicleInventory < 1:
            messages.error(request, f'Oops! {VehicleType} parking space is full')
            return render(request, 'rentBookingCreate.html')
        
    return render(request, 'rentBookingCreate.html')
