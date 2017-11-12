from django.shortcuts import render
from .models import DadoPessoal

def home(request):
    data = DadoPessoal.objects.all()
    context = {
        'data': data
    }

    return render(request, 'index.html', context)
