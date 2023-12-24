from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Project, Task


# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         help_texts = {'username': '', 'email': '', 'password': ''}


class RegistrationForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['password1'].help_text = ''
    #     self.fields['password2'].help_text = ''
    username = forms.CharField(help_text="")
    email = forms.EmailField(help_text="")
    password1 = forms.CharField(help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(help_text="", widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
    username = forms.CharField(help_text="")
    password = forms.CharField(help_text="", widget=forms.PasswordInput)


# class FilmForm(forms.Form):
#     title = forms.CharField()
#     year = forms.DateField()
#     genre = forms.CharField()


# class FilmForm1(forms.ModelForm):
#     class Meta:
#         model = Films
#         fields = ['title', 'year', 'genre']
#
#
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'description', 'year', 'author']


class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['name']

class ChangeProjectForm(forms.Form):
    name = forms.CharField()


class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = ['name', 'status', 'deadline', 'priority']
