from django.db import models

from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=20, default='Evento')
    date = models.DateField('Fecha del evento',auto_now=True)
    organizers = models.ManyToManyField(User)
