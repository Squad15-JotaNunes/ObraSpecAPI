from django.db import models

# Create your models here.

class Obra(models.Model):
    nome_empreendimento = models.CharField(max_length=250, null=False)
    localizacao = models.CharField(max_length=250, null=False)
    descricao = models.TextField(null=False)
    num_unidades_habiticionais = models.IntegerField()
    num_unidades_adaptadas = models.IntegerField()
    area_terreno = models.DecimalField(decimal_places=2)
    # modelo = models.ForeignKey(ModeloPadrao, on_delete=models.CASCADE, related_name='modelo')
    observacoes = models.ManyToManyField('Observacao')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome_empreendimento
