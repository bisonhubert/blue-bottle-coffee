from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import pgettext_lazy
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from . import CURRENCY_CHOICES

class Category(MPTTModel):
    class Meta:
        verbose_name_plural = "categories"
        
    name = models.CharField(
        pgettext_lazy('Category field', 'name'), unique=True, max_length=100)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children',
        on_delete=models.deletion.SET_NULL, default=None,
        verbose_name=pgettext_lazy('Category field', 'parent'))

    tree = TreeManager()

    def __str__(self):
        return self.name


class Item(models.Model):
    sku = models.CharField(
        pgettext_lazy('Item field', 'SKU'), 
        max_length=32, unique=True)
    category = models.ForeignKey(
        Category, verbose_name=pgettext_lazy('Item field', 'category'),
        related_name='items', on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.sku


class ItemDetail(models.Model):
    item = models.ForeignKey(
        Item, verbose_name=pgettext_lazy('Item detail field', 'item'),
        related_name='details', on_delete=models.deletion.CASCADE)
    name = models.CharField(
        pgettext_lazy('Item detail field', 'name'), max_length=100)
    currency = models.CharField(
        pgettext_lazy('Item detail field', 'currency'), max_length=5,
        choices=CURRENCY_CHOICES)
    price = models.DecimalField(
        pgettext_lazy('Item detail field', 'price'),
        max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    def get_dollar_amount(self):
        return MoneyField(
            max_digits=8, decimal_places=2, default_currency=self.currency)
