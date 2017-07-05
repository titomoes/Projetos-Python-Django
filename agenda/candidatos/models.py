from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Candidato(models.Model):

    nome = models.CharField(max_length=200)
    partido = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
