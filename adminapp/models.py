from django.db import models

# Create your models here.
class District(models.Model):
    districtid=models.AutoField(primary_key=True)
    districtname=models.CharField(max_length=50)
class Location(models.Model):
    locationid=models.AutoField(primary_key=True)
    districtid=models.ForeignKey(District,on_delete=models.CASCADE)
    locationname=models.CharField(max_length=50)
class Casetype(models.Model):
    casetypeid=models.AutoField(primary_key=True)
    casetype=models.CharField(max_length=100)
    description=models.CharField(max_length=150)



