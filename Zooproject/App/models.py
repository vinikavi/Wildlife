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
  email=models.EmailField(max_length=30)
  mobile=models.CharField(max_length=10)
  password=models.CharField(max_length=10)
class Booking(models.Model):
  name=models.CharField(max_length=20)
  email=models.EmailField(max_length=30)
  mobile=models.CharField(max_length=10)
  age=models.CharField(max_length=3)
  cost=models.CharField(max_length=10)
  total=models.IntegerField()
  child=models.IntegerField()
  adult=models.IntegerField()
  country=models.CharField(max_length=20)
  state=models.CharField(max_length=20)
  date=models.DateField()
  city=models.CharField(max_length=20)
  idproof=models.CharField(max_length=30)
  idno=models.CharField(max_length=15)
  vehicle_no=models.CharField(max_length=6)   
  reg_id=models.CharField(max_length=20)  
  my_choices=[('ONLINE','online'),('OFFLINE','offline')]
  status=models.CharField(max_length=10,choices=my_choices)
  