from django.db import models

class Devolução(models.Model):
    fornecedor = models.CharField(max_length=100)
    nota_entrada = models.CharField(max_length=100)
    itens = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    nota_saida = models.CharField(max_length=100)
    transportadora = models.CharField(max_length=100)
    frete_por = models.CharField(max_length=100)
    executada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fornecedor} - {self.fornecedor}"
