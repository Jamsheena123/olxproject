from django import forms
from task.models import Vehicles
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "owner":forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control"}),
            "kilometre":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3}),
   
    }
        

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["name","fuel_type","kilometre","price","location","description","image"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control"}),
            "kilometre":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3}),
        }