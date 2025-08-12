from django.contrib import admin
from .models import Client, ClientBill

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'list_of_bills')
    fields = ('name', 'bills')
    search_fields = ['name']

    def list_of_bills(self, obj):
        return ", ".join(bill.number for bill in obj.bills.all().distinct())

# admin.site.register(ClientBill)