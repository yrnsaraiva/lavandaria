# Generated by Django 5.1.5 on 2025-02-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='cor',
        ),
    ]
