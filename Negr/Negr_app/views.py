from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    names = ['Nazar', 'Sasha', "Olga"]
    name = 'Bob'
    context = {'name': name, 'title': 'Home', 'names': names}
    return render(request, 'home.html', context)
