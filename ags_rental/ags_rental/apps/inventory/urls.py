from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import case_template, CaseView, CaseDetailView, CaseListView

urlpatterns = [
    path('cases/', CaseListView.as_view()),
    path('cases/add/', case_template),
    path('cases/<int:pk>/', CaseDetailView.as_view(), name='case-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
