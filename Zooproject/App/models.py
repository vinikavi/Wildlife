from django.db import models

# Create your models here.
class Admin(models.Model):
  name=models.CharField(max_length=30)
  username=models.CharField(primary_key=True,max_length=20)
  password=models.CharField(max_length=30)
  email=models.EmailField(max_length=30)
  mobileno=models.CharField(max_length=10)
class User(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(max_length=20)
  mobile=models.CharField(max_length=10)
  password=models.CharField(max_length=10)
class Booking(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(max_length=20)
  mobile=models.CharField(max_length=10)
  age=models.CharField(max_length=3)
  cost=models.CharField(max_length=5)
  totaltickets=models.IntegerField()
  child=models.IntegerField()
  adult=models.IntegerField()
  country=models.CharField(max_length=20)
  state=models.CharField(max_length=20)
  date=models.DateField()
  city=models.CharField(max_length=10)
  idproof=models.CharField(max_length=30)
  idno=models.CharField(max_length=20)
  vehicle_no=models.CharField(max_length=8)   
  reg_id=models.CharField(max_length=20)   