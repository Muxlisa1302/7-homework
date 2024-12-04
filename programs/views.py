from django.shortcuts import render, redirect
from .models import ProgrammingLanguage

def index(request):
    if request.method == 'POST':
        form = ProgrammingLanguage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programs_index')
    else:
        form = ProgrammingLanguage()
    return render(request, 'programs/index.html', {'form': form})
