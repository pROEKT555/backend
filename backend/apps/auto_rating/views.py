from django.shortcuts import render
from .forms import CheckForm

def index(request):
    if request.method == "POST":
        form = CheckForm(request.POST)
        if form.is_valid():
            form.save()

    form = CheckForm()
    
    data = {
        'form': form
    }
    
    return render(request, 'auto_rating/index.html', data)
