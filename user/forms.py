from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm():
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'password1','password2','email','street','city','state','country','phone_number','zip_code','is_subscribed']
        widget = {
            # 'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            # 'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'street': forms.TextInput(attrs={'placeholder': 'Street'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Confirm Password'}),
        }
        
class LoginForm():
    
    class Meta:
        model = User
        fields = ['email', 'password']        