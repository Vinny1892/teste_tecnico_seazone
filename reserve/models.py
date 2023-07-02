import uuid

from django.db import models

from announcement.models import Announcement

# Create your models here.



class Reserve(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    quantity_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.CharField(max_length=256)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
