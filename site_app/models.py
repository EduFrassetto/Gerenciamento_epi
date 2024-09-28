# models.py
from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"Colaborador: {self.nome}, data de nascimento: {self.data_nascimento}, cpf: {self.cpf}, telefone: {self.telefone}, cargo: {self.cargo}, status: {self.status}"