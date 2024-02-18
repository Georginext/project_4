from django.shortcuts import render
from django.views.generic import ListView, DetailView
from games.models import Game
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from accounts.forms import Form
from django.urls import reverse_lazy
def view(request):
    return render(request, 'home.html')

class Lists(ListView):
    model = Game
    template_name = "home.html"
    context_object_name = 'game_list'
class Info(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'menu.html'
    context_object_name = 'game'

    
    
    


# Create your views here.
