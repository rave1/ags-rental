from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from accounts.forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
# Create your views here.


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('rental-list')
    template_name = 'auth/register.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'auth/login.html'
    
    def get_success_url(self):
        return reverse_lazy('rental-list') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
