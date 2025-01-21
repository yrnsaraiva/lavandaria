from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


# Modelo para Lavandarias
class Lavandaria(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gerente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lavandarias_gerenciadas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


# Modelo para Funcionários
class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario')
    lavandaria = models.ForeignKey(Lavandaria, on_delete=models.CASCADE, related_name='funcionarios')
    funcao = models.CharField(max_length=255, null=True, choices=[
        ('gerente', 'gerente'),
        ('caixa', 'caixa')
    ])
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.funcao}"


# Modelo para Tipos de Artigos (Item de Serviço)
class ItemServico(models.Model):
    image = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=255)
    disponivel = models.BooleanField(default=True)

    def imagem(self):
        if self.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', self.image.url)
        return "Sem Imagem"

    def __str__(self):
        return f"{self.nome}"


# Modelo para Serviços Disponíveis na Lavandaria
class Servico(models.Model):
    lavandaria = models.ForeignKey(Lavandaria, on_delete=models.CASCADE, related_name='servicos')
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.lavandaria.nome}"


# Modelo para Clientes
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


# Modelo Pedido
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    lavandaria = models.ForeignKey(Lavandaria, on_delete=models.CASCADE, related_name='pedidos')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_total(self):
        self.total = sum(item.preco_total for item in self.itens.all())
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - {self.lavandaria.nome}"


# Modelo ItemPedido
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='itens')
    item_de_servico = models.ForeignKey(ItemServico, on_delete=models.CASCADE, related_name='itens', null=True, blank=True)
    quantidade = models.PositiveIntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcula o preço total com base no preço base do serviço e na quantidade
        self.preco_total = self.quantidade * self.servico.preco_base
        super().save(*args, **kwargs)
        # Atualiza o total do pedido imediatamente
        self.pedido.calcular_total()

    def delete(self, *args, **kwargs):
        # Antes de excluir o item, recalcula o total do pedido
        pedido = self.pedido  # Mantém a referência do pedido
        super().delete(*args, **kwargs)
        pedido.calcular_total()

    def __str__(self):
        return f"{self.servico.nome} - {self.quantidade}x - Total: {self.preco_total}"
