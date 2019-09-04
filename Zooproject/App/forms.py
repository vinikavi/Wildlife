from django import forms
from django.core import validators
from .models import Admin,User,Booking
class AdminRegister(forms.Form):
    name=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    mobileno=forms.CharField(max_length=10)
    def clean_password(self):
        inputname=self.cleaned_data['password']
        if len(inputname) < 8:
           raise forms.ValidationError('password must contains atleast 8 characters')
        return inputname
class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegister(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    mobileno=forms.CharField(max_length=10)
class userLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class TicketBooking(forms.ModelForm):
    class Meta:
        model=Booking
        # fields='__all__ '
        fields=['name','email','mobile','age','total','cost','child','adult','country','state','date','city','idproof','idno','vehicle_no']
        exclude=['cost','total']
