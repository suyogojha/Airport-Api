from django.db import models

import schedule
from schedule.models import Flight
# Create your models here.
class Status(models.Model):
    pnr=models.CharField(max_length=10,primary_key=True)
    boardstatus=models.CharField(max_length=10)
    description=models.CharField(max_length=10)
class Passenger(models.Model):
    name=models.CharField(max_length=20)
    pnr=models.ForeignKey('Status',on_delete=models.CASCADE)
    flightid=models.CharField(max_length=5)
    source=models.CharField(max_length=4)
    destination=models.CharField(max_length=4)
class Goods(models.Model):
    item = models.CharField(max_length=20)
    pnr = models.ForeignKey('Status',on_delete=models.CASCADE)
    flightid = models.CharField(max_length=5)
    source = models.CharField(max_length=4)
    destination = models.CharField(max_length=4)
class LiveFlight(models.Model):
    flightid=models.ForeignKey('schedule.Flight',on_delete=models.CASCADE)
    status=models.CharField(max_length=30)
