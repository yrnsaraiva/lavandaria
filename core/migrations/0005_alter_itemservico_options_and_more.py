# Generated by Django 5.1.5 on 2025-02-09 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_itempedido_servico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemservico',
            options={'verbose_name': 'Artigo', 'verbose_name_plural': 'Artigos'},
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='item_de_servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itens', to='core.itemservico', verbose_name='Artigo'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='servico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itens', to='core.servico'),
        ),
    ]
