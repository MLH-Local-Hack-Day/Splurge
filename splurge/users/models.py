from django.db import models

from django.contrib.auth.models import User

from communities.models import Event

class AppUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    organizer = models.BooleanField(blank=True, default=False)
    events = models.ManyToManyField(Event)

    def __str__(self):
       return '@' + str(self.user)
