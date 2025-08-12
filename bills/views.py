from django.views import generic
from .models import Bill
# Create your views here.
class BillListView(generic.ListView):
    model = Bill

class BillupdateView(generic.UpdateView):
    model = Bill