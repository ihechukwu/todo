from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task
from django.forms.widgets import PasswordInput, TextInput


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateTaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']