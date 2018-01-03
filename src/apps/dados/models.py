from django.db import models
from .data import LISTA_MESES  # Combobox


class DadoPessoal(models.Model):
    title = models.CharField(max_length=40, verbose_name='Título')
    description = models.TextField(max_length=500, verbose_name='Descrição')
    dia_evento = models.IntegerField(
        verbose_name='Dia da Ocorrência'
    )
    mes_evento = models.PositiveSmallIntegerField(
        choices=LISTA_MESES,
        default=1,
        verbose_name='Mês da Ocorrência',
    )
    ano_evento = models.CharField(
        max_length=4,
        verbose_name='Ano da Ocorrência'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Dado Pessoal'
        verbose_name_plural = 'Dados Pessoais'

    def __str__(self):
        return self.title
