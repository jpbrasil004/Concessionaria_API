from django.db import models

class Montadora (models.Model):
    nome = models.CharField(max_length=200)
    bio = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Modelo (models.Model):
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nome