from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Pedido
from django.shortcuts import redirect


# def index(request):
#     return redirect('admin/')
#

def gerar_recibo_pdf(request, pedido_id):
    # Obter o pedido pelo ID
    pedido = Pedido.objects.get(id=pedido_id)

    # Renderizar o template HTML com os dados do pedido
    template = get_template('core/recibo_pedido.html')
    html = template.render({'pedido': pedido})

    # Criar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="recibo_pedido_{pedido_id}.pdf"'

    # Converter HTML para PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verificar erros
    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=500)

    return response
