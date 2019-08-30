from django import forms
from .models import Admin,User,Booking
class AdminRegister(forms.Form):
    name=forms.CharField()
    username=forms.CharField()
    password=forms.CharField()
    email=forms.EmailField()
    mobileno=forms.CharField()
class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class UserRegister(forms.Form):
    name=forms.CharField()
    password=forms.CharField()
    email=forms.EmailField()
    mobileno=forms.CharField()
class userLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class TicketBooking(forms.ModelForm):
    class Meta:
        model=Booking
        # fields='__all__ '
        fields=['name','email','mobile','age','cost','totaltickets','country','state','date','city','passport','vehicle_no']
        exclude=['cost']
