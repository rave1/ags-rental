from django.urls import path

from rental.views import rental_view, RentalList, RentalDetail

urlpatterns = [
    path('rentals/', RentalList.as_view(), name='rental-list'),
    path('rentals/<int:pk>', RentalDetail.as_view(), name='rental-detail')
]
