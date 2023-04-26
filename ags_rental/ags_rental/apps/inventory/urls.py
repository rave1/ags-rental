from django.urls import path

from inventory.views import case_template, CaseView

urlpatterns = [
    path('case/', CaseView.as_view())
]
