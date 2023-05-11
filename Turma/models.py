from django.db import models

# Create your models here.

class Turma(models.Model):

    Codigo  = models.CharField(max_length=100)
    CodigoCurso = models.IntegerField(max_length=100)
    