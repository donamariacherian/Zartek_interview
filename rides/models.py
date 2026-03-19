from django.db import models

# Create your models here.
class Rides(models.Model):
    status_choices=[ ('STARTED', 'Started'),('COMPLETED', 'Completed'),('CANCELLED', 'Cancelled'),]
    rider=models.CharField(max_length=20)
    driver=models.CharField(max_length=30)
    pickuplocation=models.TextField()
    dropofflocation=models.TextField()
    status=models.CharField(max_length=20,choices=status_choices)
    createdat=models.DateTimeField(auto_now=True)
    updatedat=models.DateTimeField(auto_now=True)
    lattitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)