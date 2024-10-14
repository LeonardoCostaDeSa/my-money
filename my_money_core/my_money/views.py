from django.shortcuts import render
from my_money.models import Transaccoes_de_saida

def mostrar_transacoes_de_saida(request):
    mostrar_transacoes_de_saida=Transaccoes_de_saida.objects.all()
    return render(request, 'index.html', {"data": mostrar_transacoes_de_saida})
