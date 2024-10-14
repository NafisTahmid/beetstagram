from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget = forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude = ['user','username',]
    