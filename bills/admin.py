from django.contrib import admin
from .models import Bill

# Register your models here.


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'clients_list')
    fields = ('title', 'number', 'clients')
    search_fields = ['title', 'number']

    def clients_list(self, obj=None):
        return ", ".join(f'{client}' for client in obj.clients.all())