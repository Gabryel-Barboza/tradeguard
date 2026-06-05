from django.shortcuts import get_object_or_404, render

from .models import Contract

# Create your views here.


def get_contracts(request):
    contracts = Contract.objects.select_related('supplier').all()

    context = {'contracts': contracts}

    return render(request, 'management/listContracts.html', context)


def get_contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)

    context = {'contract': contract}

    return render(request, 'management/contractDetail.html', context)
