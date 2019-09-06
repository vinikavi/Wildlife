from django import forms
from django.core import validators
from .models import Admin,User,Booking
class DateInput(forms.DateInput):
    input_type = 'date'
class AdminRegister(forms.Form):
    name=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(max_length=30)
    mobileno=forms.CharField(max_length=10)
    def clean_password(self):
        inputname=self.cleaned_data['password']
        if len(inputname) < 8:
           raise forms.ValidationError('password must contains atleast 8 characters')
        return inputname
class Login(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class UserRegister(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(max_length=30)
    mobileno=forms.CharField(max_length=10)
class userLogin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class TicketBooking(forms.ModelForm):
    class Meta:
        model=Booking
        # fields='__all__ '
        fields=['name','email','mobile','age','total','parks_names','cost','child','status','adult','country','state','date','city','idproof','idno','vehicle_no']
    
        exclude=['cost','total']
        widgets = {
            'date': DateInput(),
            }