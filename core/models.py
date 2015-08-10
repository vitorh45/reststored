from django.db import models


class Zipcode(models.Model):

    zipcode = models.CharField(max_length=8, unique=True)
    address = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)