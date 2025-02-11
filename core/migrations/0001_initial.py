# Generated by Django 5.1.5 on 2025-02-07 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20, unique=True)),
                ('endereco', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lavandaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=20, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=20, unique=True)),
                ('grupo', models.CharField(choices=[('gerente', 'Gerente'), ('caixa', 'Caixa')], help_text='Define o grupo do usuário.', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL)),
                ('lavandaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='core.lavandaria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('pronto', 'Pronto')], default='pendente', max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pago', models.BooleanField(default=False)),
                ('metodo_pagamento', models.CharField(choices=[('numerario', 'Numerário'), ('pos', 'POS (Cartão)'), ('conta_movel', 'Conta Movel'), ('mpesa', 'M-Pesa'), ('emola', 'e-Mola'), ('outro', 'Outro')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.cliente')),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos', to='core.funcionario')),
                ('lavandaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.lavandaria')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('lavandaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicos', to='core.lavandaria')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cor', models.CharField(choices=[('branco', 'Branco'), ('preto', 'Preto'), ('azul', 'Azul'), ('vermelho', 'Vermelho'), ('verde', 'Verde'), ('amarelo', 'Amarelo'), ('laranja', 'Laranja'), ('roxo', 'Roxo'), ('rosa', 'Rosa'), ('castanho', 'Castanho'), ('cinza', 'Cinza')], max_length=20)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('item_de_servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itens', to='core.itemservico')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.pedido')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.servico')),
            ],
        ),
    ]
