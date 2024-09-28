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
    status = models.CharField(max_length=10)

    def __str__(self):
        return (f"Epi: {self.nome_epi}, marca: {self.marca}, modelo: {self.modelo}, lote: {self.lote}, "
                f"validade: {self.validade}, validade_uso: {self.validade_uso}, status: {self.status}")
    
class Emprestimo(models.Model):
    STATUS_CHOICES = [
        (1, 'Emprestado'),
        (2, 'Em uso'),
        (3, 'Fornecido'),
        (4, 'Devolvido'),
        (5, 'Danificado'),
        (6, 'Perdido'),
    ]
    epi = models.ForeignKey(Epi, on_delete=models.CASCADE, related_name="equipamento")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="colaborador")
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    status = models.CharField(
        max_length= 10,
        choices=STATUS_CHOICES,
        default=1)
   
    def __str__(self):
        return (f"Equipamento: {self.epi}, Colaborador: {self.colaborador}, Data emprestimo: {self.data_emprestimo}, "
        f"Data devolução: {self.data_devolucao}, Status: {self.status}")
