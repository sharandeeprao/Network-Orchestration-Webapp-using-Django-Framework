from django.db import models

class InventoryData(models.Model):
    Hostname = models.CharField(max_length=100)
    IPaddress = models.GenericIPAddressField()
