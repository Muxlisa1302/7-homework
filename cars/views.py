from django.shortcuts import render, redirect
from .models import Car

def index(request):
    if request.method == 'POST':
        form = Car(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars_index')
    else:
        form = Car()
    return render(request, 'cars/index.html', {'form': form})
