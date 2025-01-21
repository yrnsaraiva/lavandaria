from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ItemPedido


# Atualizar o total do pedido ao adicionar ou modificar um item
@receiver(post_save, sender=ItemPedido)
def atualizar_total_apos_salvar(sender, instance, **kwargs):
    instance.pedido.calcular_total()


# Atualizar o total do pedido ao excluir um item
@receiver(post_delete, sender=ItemPedido)
def atualizar_total_apos_excluir(sender, instance, **kwargs):
    instance.pedido.calcular_total()
