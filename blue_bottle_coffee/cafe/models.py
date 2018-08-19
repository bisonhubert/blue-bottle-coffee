from django.db import models
from django.utils.translation import pgettext_lazy

class Cafe(models.Model):
    name = models.CharField(
        pgettext_lazy('Cafe field', 'name'),
        max_length=100)
    address = models.CharField(
        pgettext_lazy('Cafe field', 'address'),
        max_length=200)
    country = models.CharField(
        pgettext_lazy('Cafe field', 'country'),
        max_length=3)

    def __str__(self):
        return self.name
