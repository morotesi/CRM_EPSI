from django.db import models

"""
Marque
#######
id
label
"""


class Marque(models.Model):
    label = models.CharField(max_length=56)
