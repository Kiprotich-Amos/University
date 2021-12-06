from django.db.models.base import Model
from django.forms import ModelForm, fields, models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


from .models import Placement
class StudentPlacementForm(ModelForm):
    class Meta:
        model = Placement
        fields = '__all__'

from .models import Student
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']