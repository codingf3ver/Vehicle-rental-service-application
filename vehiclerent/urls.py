from django.urls import path,include
from . import views

urlpatterns = [ 
    path('', views.home, name='home'), # home page view
    path('customer/', views.customerCreate, name='customerCreate'), # register customer info page view
    path('rentbooking', views.rentBookingCreate, name='rentBookingCreate'), # rent booking page
]
