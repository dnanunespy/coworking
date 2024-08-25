# reservas/models.py
from django.db import models
from django.contrib.auth.models import User


class EspacoCoworking(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    descricao = models.TextField()
    capacidade = models.IntegerField()
    preco_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return self.nome  # Exibir o nome do espaço de coworking


class Reserva(models.Model):
    espaco = models.ForeignKey(EspacoCoworking, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    data_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.espaco.nome} - {self.data_reserva} - {self.hora_inicio} to {self.hora_fim}"
