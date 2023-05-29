from django.urls import path

from rental.views import rental_view, RentalList, RentalDetail, CreateRentalView, RentalFormView, RentalInvoiceView

urlpatterns = [
    path('rentals/', RentalList.as_view(), name='rental-list'),
    path('rentals/<int:pk>', RentalDetail.as_view(), name='rental-detail'),
    path('create-rental/', CreateRentalView.as_view(), name='rental-create'),
    path('add-rental/', RentalFormView.as_view(), name='rental-form'),
    path('rental-invoice/<int:pk>/', RentalInvoiceView.as_view(), name='rental-invoice')
]
