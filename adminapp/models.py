
from django.db import models
class Booking(models.Model):
    name=models.CharField(max_length=40)
    address=models.TextField()
    contactno=models.CharField(max_length=10)
    aadhaarno=models.CharField(max_length=12,primary_key=True)
    noofpacket=models.IntegerField() #input to Accounting to  farmer
    duration=models.IntegerField()   #input to Accounting to  farmer
    rate=models.IntegerField()       #input to Accounting to admin
    totalamt=models.IntegerField()
    advance=models.IntegerField()   #input to Accounting to  farmer
    restamt=models.IntegerField()
    bookingdate=models.CharField(max_length=30)

class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)

class mBooking(models.Model):
    name=models.CharField(max_length=14)
    firmname=models.CharField(max_length=100)
    firmaddress=models.TextField()
    contactno=models.CharField(max_length=10)
    aadhaarno=models.CharField(max_length=12,primary_key=True)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    demand=models.CharField(max_length=20)
    ninkg=models.IntegerField() #input to Accounting to Merchant
    rate=models.IntegerField() #input to Accounting to admin
    totalamt=models.IntegerField()
    advance=models.IntegerField()#input to Accounting to  merchant
    restamt=models.IntegerField()
    bookingdate=models.CharField(max_length=30)



