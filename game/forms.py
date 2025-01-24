from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import MissingReview

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-item'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-item'}), required=True)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password")
        return self.cleaned_data

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})


    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = MissingReview
        fields = ['game', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].widget.attrs.update({'placeholder': 'voer graag de naam van het spel in (tot 3 spellen per keer)(, tussen de spellen)'})
        self.fields['game'].required = True
        self.fields['comment'].widget.attrs.update({'placeholder': 'waarom wil je dit spel graag zien?'})
        self.fields['comment'].required = True