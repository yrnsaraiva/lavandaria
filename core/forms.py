from django import forms
from django.utils.html import format_html
from .models import ItemPedido, ItemServico


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'servico', 'item_de_servico', 'quantidade', 'preco_total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizando o widget para mostrar a imagem do item de serviço
        self.fields['item_de_servico'].widget.choices = self.get_choices_with_images()

    def get_choices_with_images(self):
        choices = []
        for item in ItemServico.objects.all():
            if item.image:
                image_html = f'<img src="{item.image.url}" width="50" height="50" style="object-fit: cover; margin-right: 10px;" />'
                display_name = f"{image_html} {item.nome}"
            else:
                display_name = f"Sem Imagem {item.nome}"

            choices.append((item.id, display_name))
        return choices
