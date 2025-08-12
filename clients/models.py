from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Client(models.Model):
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        default_related_name = 'clients'

    name = models.CharField(max_length=150)
    bills = models.ManyToManyField('bills.Bill', through='ClientBill', related_name='client_set', help_text=_('Bills'), blank=True, symmetrical=True)

    def __str__(self):
        return f'{self.name}'


class ClientBillManager(models.Manager):
    pass

class ClientBill(models.Model):
    class Meta:
        verbose_name = _('ClientBill')
        verbose_name_plural = _('ClientBills')
        default_related_name = 'clientbills'
        auto_created = True


    client = models.ForeignKey(Client, on_delete=models.CASCADE, help_text=_('Client'))
    bill = models.ForeignKey('bills.Bill', on_delete=models.CASCADE, help_text=_('Bill'))
    date_of_relation = models.DateField( auto_now_add=True, help_text=_('Date of relation'))
    priority = models.IntegerField(default=3)

    objects = ClientBillManager()