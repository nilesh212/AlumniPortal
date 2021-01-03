from django import forms
from app.models import SignUpModel,PostModel,EventModel
from django.contrib.auth.models import User
from django.db import models



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields =('username','password','email','first_name','last_name')



class SignUpForm(forms.ModelForm):
    class Meta():
        model = SignUpModel
        fields = ('roll_number','graduation_year')



class PostForm(forms.ModelForm):
    class Meta():

        model = PostModel
        fields = ('title','info')



class EventForm(forms.ModelForm):
    class Meta():
        model = EventModel
        fields=('photo','title','text')



