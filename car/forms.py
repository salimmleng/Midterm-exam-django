from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import CarModel,Brand,Comment,Profile
from django import forms 

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class CarmodelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']



class ChangeuserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']

