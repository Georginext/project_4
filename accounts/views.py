from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import Form
from django.views.generic import CreateView

class Registration(CreateView):
    form_class = Form
    success_url = reverse_lazy("login")
    template_name = "register.html"

# Create your views here.
