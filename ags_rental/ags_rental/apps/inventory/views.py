from django.http import HttpResponse
from django.template import loader
from inventory.forms import CaseForm
from django.shortcuts import render
from django.views import View

# Create your views here.


def case_template(request):
    if request.POST:
        form = CaseForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        form.save()
    context = {'article_form': CaseForm}
    return render(request, 'case_form.html', context)


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