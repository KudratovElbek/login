from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarForm


def cars_list(request):
    cars = Cars.objects.all()  # Retrieve all planets from the database
    return render(request, 'Cars.html', {'cars': cars})