from django.urls import path,include
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('customer/', views.customerCreate, name='customerCreate'),
    # path('customerlist', views.customerList, name='customerList'),
    path('rentbooking', views.rentBookingCreate, name='rentBookingCreate'),
]