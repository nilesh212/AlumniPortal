from django import forms
from app.models import SignUpModel,PostModel,EventModel,EventComment
from django.contrib.auth.models import User
from django.db import models



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'input_align'}))

    class Meta():
        model=User
        fields =('username','password','email','first_name','last_name')

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Username','class':'input_align'}),

            'email': forms.TextInput(attrs={'placeholder': 'Enter your Email Id','class':'input_align'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your Name','class':'input_align'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter AdminCode *(only,if you are Admin)','class':'input_align'}),

        }



class SignUpForm(forms.ModelForm):
    class Meta():
        model = SignUpModel
        fields = ('roll_number','graduation_year')

        widgets = {
            'roll_number':forms.TextInput(attrs={'placeholder':'Enter your Roll number','class':'input_align'}),
            'graduation_year':forms.TextInput(attrs={'placeholder':'Graduation Year','class':'input_align'}),

        }



class PostForm(forms.ModelForm):
    class Meta():

        model = PostModel
        fields = ('title','info')

        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Title','class':'input_align'}),
            'info': forms.Textarea(attrs={'class': 'textarea_align','placeholder':'Post Information'})
        }



class EventForm(forms.ModelForm):
    class Meta():
        model = EventModel
        fields=('photo','title','text')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title','class':'input_align'}),
            'text':forms.Textarea(attrs={'class':'textarea_align','placeholder':'Event Information'})
        }



class EventCommentForm(forms.ModelForm):
    class Meta():
        model=EventComment
        fields=['comment']

        widgets = {
            'comment':forms.Textarea(attrs={'placeholder':'Comment','class':'textarea_align'})
        }
