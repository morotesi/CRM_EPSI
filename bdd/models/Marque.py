from django.db import models

"""
Marque
#######
id
label
"""


class Marque(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=56)
