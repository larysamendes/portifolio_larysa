from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    tipo = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo

class Plataforma(models.Model):
    nomePla = models.CharField(max_length=40)
    def __str__(self):
        return self.nomePla

class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Jogo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=40)
    data = models.DateField()
    genero = models.ManyToManyField(Genero)
    plataforma = models.ManyToManyField(Plataforma)
    enredo = models.TextField()
    critica = models.TextField()
    avaliacao = models.IntegerField(max_length=5)
    desenvolvedores = models.ManyToManyField(Desenvolvedor)
    capa_jogo= models.ImageField(upload_to='capas/%d/%m/%Y', blank=True)

    publicar = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

