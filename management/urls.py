from django.urls import path

from .views import get_contract_detail, get_contracts

urlpatterns = [
    path('', get_contracts, name='list-contracts'),
    path('<uuid:pk>/', get_contract_detail, name='contract-detail'),
]
