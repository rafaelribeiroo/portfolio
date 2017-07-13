from django.shortcuts import render
from .models import DadoPessoal

def home(request):
    data = {}
    data['listar_dados'] = DadoPessoal.objects.all()
    context = {
        'data': data
    }

    return render(request, 'index.html', context)
