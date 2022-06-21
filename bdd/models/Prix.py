from django.db import models

class Prix(models.Model):
    id = models.IntegerField(primary_key=True)
    id_voiture = models.IntegerField()
    prix = models.FloatField(max_length=56)
    date_start = models.DateField()
    date_stop = models.DateField(null=True, blank=True)

    class Meta():
        verbose_name = "Prix"
        verbose_name_plural = "Prix"