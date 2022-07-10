from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order


class Organization(models.Model):
    """ Organization model """
    name = models.CharField(max_length=254, unique=True)
    description = description = models.TextField()
    url = models.URLField(max_length=128, unique=True)
    donation_url = models.URLField(max_length=128, unique=True)
    logo = models.ImageField()

    def __str__(self):
        return self.name
