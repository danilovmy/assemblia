from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Bill(models.Model):
    class Meta:
        verbose_name = _('Bill')
        verbose_name_plural = _('Bills')
        default_related_name = 'bills'

    title = models.CharField(max_length=150, help_text=_('Title of the bill'))
    number = models.CharField(max_length=150, unique=True, help_text=_('Title of the bill'))
    clients = models.ManyToManyField('clients.Client', through='clients.ClientBill', related_name='bill_set', help_text=_('Clients'), blank=True, symmetrical=True)

    def __str__(self):
        return f'{self.number}'

    @property
    def opts(self):
        return self._meta