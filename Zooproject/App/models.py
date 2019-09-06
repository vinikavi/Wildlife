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
    parks=(
          ('Queen Elizabeth national park','Queen Elizabeth national park'),
          ('Murchison falls national park','Murchison falls national park'),
          ('Bwindi impenetrable national park','Bwindi impenetrable national park'),
          ('Lake Mburo national Park','Lake Mburo national Park'),
          ('Kidepo Valley National Park','Kidepo Valley National Park'),
          ('Semuliki National Park','Semuliki National Park'),
          ('Mt Elgon National Park','Mt Elgon National Park'),
          ('Mgahinga Gorilla National Park','Mgahinga Gorilla National Park')
          
      )
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    parks_names=models.CharField(max_length=35,choices=parks)
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
  