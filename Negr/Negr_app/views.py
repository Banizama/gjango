from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Directors, Films, Book
from .forms import FilmForm1, BookForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    user = request.user
    context = {'username': user}
    return render(request, 'home.html', context)


def about(request):
    context = {'first_name': 'Nazar', 'second_name': 'Ovsienko', 'age': 17, 'city': 'Kyiv'}
    return render(request, 'aboutMe.html', context)


def page1(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        surname = data['surname']
        age = data['age']
        director = Directors(first_name=name, second_name=surname, age=age)
        director.save()
    return render(request, 'page1.html')


def page2(request):
    dirs = Directors.objects.all()
    return render(request, 'page2.html', {'data': dirs})


def page3(request):
    if request.method == 'POST':
        form = FilmForm1(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            genre = form.cleaned_data['genre']
            # poster = form.cleaned_data['poster']
            dir = Directors.objects.get(id=1)
            film = Films(title=title, year=year, genre=genre, director=dir)
            film.save()
        return render(request, 'page3.html', {'form': form})
    else:
        form = FilmForm1()
        return render(request, 'page3.html', {'form': form})


def films(request):
    film = Films.objects.all()
    return render(request, 'films.html', {'films': film})


def books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            year = form.cleaned_data['year']
            author = form.cleaned_data['author']
            book = Book(title=title, description=description, year=year, author=author)
            book.save()
        return render(request,'books.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'books.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        return render(request, 'registration.html', context={'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', context={'form': form})


def login1(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username,  password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})