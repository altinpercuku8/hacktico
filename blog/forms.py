from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import PostModel
from django import forms
from django.core.validators import EmailValidator

# Modeli i perdoruesve

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Modeli i postimeve

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'image_url','content',]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator])
    subject = forms.CharField(max_length=200)
    message  = forms.CharField(widget=forms.Textarea)