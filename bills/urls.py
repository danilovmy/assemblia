from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views import generic
from .views import BillListView

urlpatterns = [
    path("", BillListView.as_view(), name="bills_list"),
]
