from django.db import models
from adminapp.models import *
from datetime import date
class Login(models.Model):
    loginid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
class Advocate(models.Model):
    advocateid=models.AutoField(primary_key=True)
    advocatename=models.CharField(max_length=50)
    emailid=models.CharField(max_length=150)
    contactnumber = models.BigIntegerField()
    casetypeid = models.ForeignKey(Casetype, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='images/')
    license=models.ImageField()
    experience=models.BigIntegerField()
    licensenumber=models.BigIntegerField()
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)

# Create your models here.



class Client(models.Model):
    clientid=models.AutoField(primary_key=True)
    clientname=models.CharField(max_length=50)
    districtid = models.ForeignKey(District, on_delete=models.CASCADE)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    housename=models.CharField(max_length=150)
    pincode= models.BigIntegerField()
    emailid = models.CharField(max_length=150)
    contactnumber = models.CharField(max_length=150)
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE)

class Casedetails(models.Model):
    casedetailsid=models.AutoField(primary_key=True)
    advocateid = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    casetypeid = models.ForeignKey(Casetype, on_delete=models.CASCADE)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    casetitle = models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    requeststatus= models.CharField(max_length=150)
    filedetails = models.FileField()
    amount =models.BigIntegerField()
    submitedate=models.DateField(default=date.today)

class Sitting(models.Model):
    sittingid=models.AutoField(primary_key=True)
    sittingamount =models.BigIntegerField()
    casedetailsid=models.ForeignKey(Casedetails, on_delete=models.CASCADE)
    advocateid = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    submitedate=models.DateField()
    sittingdescription=models.CharField(max_length=150)

class SittingPayment(models.Model):
      sittingid = models.ForeignKey(Sitting, on_delete=models.CASCADE)
      paymentdescription = models.CharField(max_length=150)
      paymentdate = models.DateField()
      paymentstatus = models.CharField(max_length=150)

class Cases(models.Model):
    casestatusid=models.AutoField(primary_key=True)
    casedetailsid=models.ForeignKey(Casedetails, on_delete=models.CASCADE)
    advocateid = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    statusdescription= models.CharField(max_length=150)
    updateddate=models.DateField()
    nextdate=models.DateField()