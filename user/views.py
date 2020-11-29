from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
# from .models import Customer
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    #fields = ('username','password','confirm_password','first_name','last_name','email','gender','birthday')
    template_name = 'signup.html'

# class CustomerView(CreateView):
#     model = Customer
#     fields = '__all__'
#     template_name = 'signup.html'
