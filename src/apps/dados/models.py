from django.db import models
#from .data import LISTA_MESES  # Combobox

JAN = 1
FEV = 2
MAR = 3
ABR = 4
MAI = 5
JUN = 6
JUL = 7
AGO = 8
SET = 9
OUT = 10
NOV = 11
DEZ = 12
LISTA_MESES = (
    (JAN, 'Janeiro'),
    (FEV, 'Fevereiro'),
    (MAR, 'Março'),
    (ABR, 'Abril'),
    (MAI, 'Maio'),
    (JUN, 'Junho'),
    (JUL, 'Julho'),
    (AGO, 'Agosto'),
    (SET, 'Setembro'),
    (OUT, 'Outubro'),
    (NOV, 'Novembro'),
    (DEZ, 'Dezembro'),
)


class DadoPessoal(models.Model):
    title = models.CharField(max_length=40, verbose_name='Título')
    description = models.TextField(max_length=500, verbose_name='Descrição')
    dia_evento = models.CharField(
        max_length=2,
        verbose_name='Dia da Ocorrência'
    )
    mes_evento = models.PositiveSmallIntegerField(
        choices=LISTA_MESES,
        default=JAN,
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
