from django.db import models

from immobile.models import Immobile

# Create your models here.


class Announcement(models.Model):
    tax_platform = models.DecimalField(max_digits=6, decimal_places=2)
    name_platform = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE)

    @property
    def reserve(self):
        return self.reserve_set.all()
