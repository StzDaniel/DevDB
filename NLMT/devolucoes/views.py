from django.shortcuts import render, redirect
from .models import Devolução
from .forms import DevoluçãoForm

def lista_devoluções(request):
    fornecedor_query = request.GET.get('fornecedor_query', '')
    nota_entrada_query = request.GET.get('nota-entrada', '')
    itens_query = request.GET.get('itens', '')
    quantidade_query = request.GET.get('quantidade', '')
    nota_saida_query = request.GET.get('nota_saida', '')
    transportadora_query = request.GET.get('transportadora', '')
    frete_por_query = request.GET.get('frete_por', '')
    status_filter = request.GET.get('status', '')  

    Devoluções = Devolução.objects.all()

    if fornecedor_query:
        Devoluções = Devoluções.filter(os__icontains=fornecedor_query)
    if nota_entrada_query:
        Devoluções = Devoluções.filter(nota__icontains=nota_entrada_query)
    if itens_query:
        Devoluções = Devoluções.filter(itens__icontains=itens_query)
    if quantidade_query:
        Devoluções = Devoluções.filter(quantidade__icontains=quantidade_query)
    if transportadora_query:
        Devoluções = Devoluções.filter(transportadora__icontains=transportadora_query)
    if nota_saida_query:
        Devoluções = Devoluções.filter(nota__icontains=nota_saida_query)
    if frete_por_query:
        Devoluções = Devoluções.filter(nota__icontains=frete_por_query)

    if status_filter == 'executadas':
        Devoluções = Devoluções.filter(executada=True)
    elif status_filter == 'pendentes':
        Devoluções = Devoluções.filter(executada=False)

    return render(request, 'Devoluções/lista_devoluções.html', {
        'Devoluções': Devoluções,
        'fornecedor_query': fornecedor_query,
        'nota_entrada': nota_entrada_query,
        'itens_query': itens_query,
        'quantidade_query': quantidade_query,
        'nota_saida': nota_saida_query,
        'transportadora_query': transportadora_query,
        'frete_por_query': frete_por_query,
        'status_filter': status_filter,
    })

def nova_devolução(request):
    if request.method == 'POST':
        form = DevoluçãoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_devoluções')
    else:
        form = DevoluçãoForm()
    
    return render(request, 'Devoluções/lista_devolucoes.html', {'form': form})
    
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Devolução

def atualizar_status(request):
    if request.method == 'POST':
        devolução_id = request.POST.get('devolução_id')
        novo_status = request.POST.get('novo_status')
        devolução = Devolução.objects.get(pk=devolução_id)
        devolução.executada = novo_status == '1'
        devolução.save()

        return JsonResponse({'message': 'Status atualizado com sucesso.'})

    return JsonResponse({'error': 'Método não permitido.'}, status=405)
