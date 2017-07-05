from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from candidatos.models import Candidato
# Create your models here.
class Evento(models.Model):
    candidatos = models.OneToOneField(
        Candidato,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    data = models.DateTimeField('date published')
    descricao = models.TextField()

    def __str__(self):
        return self.descricao
