from django.contrib import admin
from .models import Devolução

@admin.register(Devolução)
class DevoluçãoAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'nota_entrada', 'itens', 'quantidade','nota_saida', 'transportadora', 'frete_por',)
    list_filter = ('fornecedor', 'nota_entrada', 'itens', 'quantidade','nota_saida', 'transportadora', 'frete_por',)
    search_fields = ('fornecedor', 'nota_entrada', 'itens', 'quantidade','nota_saida', 'transportadora', 'frete_por',)
