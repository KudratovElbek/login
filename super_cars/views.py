from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarForm


def cars_list(request):
    cars = Cars.objects.all()  # Retrieve all planets from the database
    return render(request, 'Cars.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cars.html')  # Redirect to the planets list page
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})