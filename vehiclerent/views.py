from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from vehiclerent.models import Customer ,Inventory, RentBooking
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import InventorySerializer



def home(request):
    return render(request, 'home.html')

def customerCreate(request):
    if request.method == 'POST':
        CustomerName = request.POST['CustomerName']        
        PhoneNumber = request.POST['PhoneNumber']
        Email = request.POST['Email']
        Address = request.POST['Address']
        Customer.objects.create(CustomerName=CustomerName, PhoneNumber=PhoneNumber, Email=Email, Address=Address)
        messages.success(request, 'Congratulations! customer has successfully been added.')
        
        
    return render(request, 'customerCreate.html')


def rentBookingCreate(request):

    if request.method == 'POST':

        # form data
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

        # Vehicle inventory check
        vehicleInventory = Inventory.objects.get(VehicleType=VehicleType)
        
        if vehicleInventory.VehicleInventory>0:
            vehicleInventory.VehicleInventory -= 1
            vehicleInventory.save()
            # Rent booking create
            RentBooking.objects.create( CustomerName=CustomerName, VehicleType=VehicleType, RentDate=RentDate, ReturnDate=ReturnDate) 
            # sucess message for vehicle inventory
            messages.success(request, 'Congratulations! Rent booking has successfully been created.')
        
        if  vehicleInventory.VehicleInventory < 1:
            messages.error(request, f'Oops! {VehicleType} parking space is full')
            return render(request, 'rentBookingCreate.html')
        
    return render(request, 'rentBookingCreate.html')


class InventoryList(APIView):
    def get(self,request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
