from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('print/<int:pedido_id>/', views.gerar_recibo_pdf, name='gerar_recibo_pdf'),
]
