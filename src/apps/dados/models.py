from django.db import models
from .data import LISTA_MESES #Combobox

class DadoPessoal(models.Model):
    title = models.CharField(max_length=40, verbose_name='Título')
    description = models.TextField(max_length=100, verbose_name='Descrição')
    dia_evento = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Dia da Ocorrência')
    mes_evento = models.PositiveSmallIntegerField(choices=LISTA_MESES, default='Janeiro')
    ano_evento = models.CharField(max_length=3, verbose_name='Ano da Ocorrência')

    def __str__(self):
        return self.title
