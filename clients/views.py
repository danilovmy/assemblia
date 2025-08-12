from django.views.generic import ListView, UpdateView, DetailView
from .models import Client
# Create your views here.

class ClientsListView(ListView):
    model = Client

class ClientsUpdate(UpdateView):
    model = Client
    success_url = '/clients/'

class ClientsDetailView(DetailView):
    model = Client
    success_url = '/clients/'
