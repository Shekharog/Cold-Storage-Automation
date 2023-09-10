from django.db import models

class FarmerInfo(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=10)
    aadhaarno =models.CharField(max_length=12,primary_key=True)
    regdate=models.CharField(max_length=30)

class MerchantInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    firmname = models.CharField(max_length=100)
    firmaddress = models.TextField()
    contactno = models.CharField(max_length=12)
    emailaddress=models.EmailField(max_length=50)
    aadhaarno = models.CharField(max_length=12, primary_key=True)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    demand=models.CharField(max_length=20)
    regdate = models.CharField(max_length=30)

class LoginInfo(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=15)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)

