from django.db import models

class Transaccoes_de_saida(models.Model):
    data=models.DateField
    nome=models.CharField(max_length=100)
    valor=models.FloatField
    class Meta:
        db_table="transacoes_de_saida"
