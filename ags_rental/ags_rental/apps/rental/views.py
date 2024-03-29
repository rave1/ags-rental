import io

from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from rental.models import Rental
from rental.forms import RentalForm

from inventory.models import Case

# @method_decorator(login_required, name='dispatch')
# def rental_view(request):
#     buffer = io.BytesIO()

#     p = canvas.Canvas(buffer)

#     p.drawString(100, 100, "Hello world.")
#     p.showPage()
#     p.save()

#     buffer.seek(0)

#     return FileResponse(buffer, as_attachment=False, filename='hello.pdf')

@method_decorator(login_required, name='dispatch')
class RentalList(ListView):
    model = Rental

@method_decorator(login_required, name='dispatch')
class RentalDetail(DetailView):
    model = Rental

    def get(self, request, *args, **kwargs):
        # print(request.session.__dict__)
        print(request.user.is_authenticated)
        request.session['test'] = 'kurwa'
        print(request.session.__dict__)
        print(request.session['test'])
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

@method_decorator(login_required, name='dispatch')
class CreateRentalView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventory/case_list.html'

    def get(self, request):
        if 'cases' not in request.session:
            request.session['cases'] = []
        case_param = request.query_params.get('case', None)
        if case_param is not None:
            request.session['cases'].append(case_param)
            request.session.modified = True
        queryset = Case.objects.filter(id__in=request.session['cases'])
        return Response({'object_list': queryset})

@method_decorator(login_required, name='dispatch')
class RentalFormView(View):
    context = {}

    def get(self, request):
        form = RentalForm({'cases': request.session['cases']}, queryset=request.session['cases'])
        self.context['rental_form'] = form
        return render(request, 'rental_form.html', self.context)

    def post(self, request):
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
        self.context['rental_form'] = form
        return render(request, 'rental_form.html', self.context)


@method_decorator(login_required, name='dispatch')
class RentalInvoiceView(DetailView):
    template_name = 'rental/test_invoice.html'
    model = Rental

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        rental_serialized_data = model_to_dict(self.object)
        context['rental_serialized'] = rental_serialized_data
        print(context)
        return self.render_to_response(context)
