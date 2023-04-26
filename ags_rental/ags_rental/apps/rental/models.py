from django.db import models
from inventory.models import Case, Device

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Rental(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='rentals')
    created_at = models.DateTimeField(auto_now_add=True)
    cases = models.ManyToManyField(Case)
    devices = models.ManyToManyField(Device)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.person.name}, {self.created_at.date()}'
