from django.urls import path

from rental.views import rental_view

urlpatterns = [
    path('rental/', rental_view)
]
