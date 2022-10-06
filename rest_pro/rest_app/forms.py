from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *




class UserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class chefForm(forms.ModelForm):
    class Meta:
        model = chef
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address','Qualification','Experience','specialisation')


class waiterForm(forms.ModelForm):
    class Meta:
        model = waiter
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address','Qualification','Experience',)

class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address')

class foodForm(forms.ModelForm):
    class Meta:
        model = food
        fields = ('food_name', 'food_price', 'food_type','food_image')

class DateInput(forms.DateInput):
    input_type = 'date'

class paymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = ('food_name', 'food_price', 'food_type','food_image','card_number','cvv','date')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date