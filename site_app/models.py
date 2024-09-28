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
        return (f"Colaborador: {self.nome}, data de nascimento: {self.data_nascimento}, cpf: {self.cpf}, "
                f"telefone: {self.telefone}, cargo: {self.cargo}, status: {self.status}")

class Epi(models.Model):
    nome_epi = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)  # Ajustado o max_length para o campo 'marca'
    modelo = models.CharField(max_length=50)  # Corrigido o tamanho do campo modelo
    lote = models.CharField(max_length=15)
    validade = models.DateField()  # Alterado para DateField se refere a uma data de validade
    validade_uso = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return (f"Epi: {self.nome_epi}, marca: {self.marca}, modelo: {self.modelo}, lote: {self.lote}, "
                f"validade: {self.validade}, validade_uso: {self.validade_uso}, status: {self.status}")
