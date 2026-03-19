from django.db import models

# Create your models here.
class Rides(models.Model):
    rider=models.CharField(max_length=20)
    driver=models.CharField(max_length=30)
    pickuplocation=models.TextField()
    dropofflocation=models.TextField()
    status=models.CharField(max_length=20)
    createdat=models.DateTimeField(auto_now=True)
    updatedat=models.DateTimeField(auto_now=True)