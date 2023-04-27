from django.urls import path

from rental.views import rental_view, RentalList

urlpatterns = [
    path('rentals/', RentalList.as_view(), name='rental-list')
]
