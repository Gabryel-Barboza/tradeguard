from django.contrib import admin

from .models import Contract, Supplier

# Register your models here.


class ContractInline(admin.TabularInline):
    model = Contract
    extra = 1


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'contract_number',
        'contract_value',
        'contract_status',
        'description',
        'end_date',
        'supplier',
    )

    list_filter = ('contract_status', 'end_date')

    search_fields = ('contract_number', 'supplier__corporate_name')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('corporate_name', 'cnpj', 'email')

    list_filter = ('corporate_name',)

    search_fields = ('cnpj', 'corporate_name')

    inlines = (ContractInline,)
