from django import forms
from .models import Devolução

class DevoluçãoForm(forms.ModelForm):
    class Meta:
        model = Devolução
        fields = ['fornecedor', 'nota_entrada', 'itens', 'quantidade','nota_saida', 'transportadora', 'frete_por']
        labels = {
            'fornecedor': 'fornecedor',
            'nota': 'nota',
            'itens': 'itens',
            'quantidade': 'quantidade',
            'nota_saida': 'nota_saida',
            'transportadora': 'transportadora',
            'frete_por': 'frete_por',
        }
