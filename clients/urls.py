from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views import generic
from .views import ClientsListView

urlpatterns = [
    path("", ClientsListView.as_view(), name="clients_list"),
]