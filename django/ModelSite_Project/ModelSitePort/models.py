from django.db import models

# Create your models here.
class ModelSitePort(models.Model):
    modelSite = models.CharField(max_length=100, verbose_name="Model site that contains this port")
    equipmentModel = models.CharField(max_length=100, verbose_name="BBU model that contains this port")
    equipmentModelSlot = models.CharField(max_length=20, verbose_name="BBU slot that contains this port")
    BoardModel = models.CharField(max_length=20, verbose_name="Board that contains this port")
    port = models.IntegerField(verbose_name="Current port")
    portType = models.CharField(max_length=20, verbose_name="Type of current port")
    # connectionID = models.OneToOneField("to define")