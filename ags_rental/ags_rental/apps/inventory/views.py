from typing import Any, Dict
from django.urls import reverse_lazy
from inventory.forms import CaseForm, DeviceForm
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, CreateView
from inventory.models import Case, Device

# Create your views here.


def case_template(request):
    if request.POST:
        form = CaseForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        form.save()
    context = {'article_form': CaseForm}
    return render(request, 'case_form.html', context)


def add_device(request):
    if request.POST:
        form = DeviceForm(request.POST, request.FILES)
        form.save()
    context = {'device_form': DeviceForm}
    return render(request, 'device_form.html', context)


class AddDevice(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device_form.html'
    success_url = reverse_lazy('device-list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['device_form'] = self.form_class
        return context


class AddCase(CreateView):
    model = Case
    form_class = CaseForm
    template_name = 'case_form.html'
    success_url = reverse_lazy('case-list')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['case_form'] = self.form_class
        return context


class CaseView(View):
    context = {}

    def get(self, request):
        form  = CaseForm()
        self.context['article_form'] = form
        return render(request, 'case_form.html', self.context)
    
    def post(self, request):
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
        self.context['article_form'] = form
        return render(request, 'case_form.html', self.context)


class CaseListView(ListView):
    model = Case


class CaseDetailView(DetailView):
    model = Case


class DeviceListView(ListView):
    model = Device


class DeviceDetailView(DetailView):
    model = Device
