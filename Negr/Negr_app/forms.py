from django import forms
from .models import Films, Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class FilmForm(forms.Form):
    title = forms.CharField()
    year = forms.DateField()
    genre = forms.CharField()


class FilmForm1(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'year', 'genre']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'year', 'author']
