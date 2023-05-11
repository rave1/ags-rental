from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import AddCase, CaseView, CaseDetailView, CaseListView, DeviceListView, DeviceDetailView, add_device, AddDevice

urlpatterns = [
    path('cases/', CaseListView.as_view(), name='case-list'),
    path('cases/add/', AddCase.as_view(), name='case-add'),
    path('cases/<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('devices/add/', AddDevice.as_view(), name='devices-add')
]
