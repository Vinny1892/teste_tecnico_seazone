from django.db import models
from rest_framework.validators import UniqueValidator

# Create your models here.


class Immobile(models.Model):
    code = models.IntegerField(unique=True)
    quantity_toilet = models.IntegerField()
    accept_pet = models.BooleanField()
    activation_date = models.DateTimeField()
    amount_clean = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def announcement(self):
        return self.announcement_set.all()
