from django.db import models

# Create your models here.
class Flight(models.Model):
    flightid=models.CharField(max_length=5,primary_key=True)
    source=models.CharField(max_length=4)
    destination=models.CharField(max_length=4)
    Monday=models.BooleanField()
    Tuesday=models.BooleanField()
    Wednesday=models.BooleanField()
    Thursday=models.BooleanField()
    Friday=models.BooleanField()
    Saturday=models.BooleanField()
    Sunday=models.BooleanField()
    passengercap=models.IntegerField()
class Aeroplane(models.Model):
    aeroplaneid=models.CharField(max_length=10,primary_key=True)
    manufacturer=models.CharField(max_length=15)
    modelno=models.CharField(max_length=20)
    passengercap=models.IntegerField()
class Schedule(models.Model):
    flightid=models.ForeignKey('Flight',on_delete=models.CASCADE)
    source=models.CharField(max_length=4)
    destination=models.CharField(max_length=4)
    arrival=models.TimeField()
    departure=models.TimeField()
    class Meta:
        unique_together=(('flightid','source'),)