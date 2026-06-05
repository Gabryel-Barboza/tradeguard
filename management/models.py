import uuid

from django.db import models

# Create your models here.


class Supplier(models.Model):
    id = models.UUIDField(
        'Identificador', primary_key=True, default=uuid.uuid4, editable=False
    )
    corporate_name = models.CharField(
        'Razão Social', null=False, blank=False, max_length=100
    )
    cnpj = models.CharField('CNPJ', unique=True, max_length=14)
    email = models.EmailField('Email de Contato', unique=True)
    created_at = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ('-created_at',)

    def __str__(self):
        return self.corporate_name


class Contract(models.Model):
    class ContractStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Ativo'
        SUSPENDED = 'SUSPENDED', 'Suspenso'
        TERMINATED = 'TERMINATED', 'Encerrado'

    id = models.UUIDField(
        'Identificador', primary_key=True, default=uuid.uuid4, editable=False
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='contracts',
        verbose_name='Fornecedor',
    )
    contract_number = models.CharField('Número do Contrato', max_length=50)
    description = models.TextField('Descrição do Contrato')
    contract_value = models.DecimalField(
        'Valor do Contrato', max_digits=12, decimal_places=2
    )
    document = models.FileField('Conteúdo em Mídia', upload_to='contracts/%Y/%m')
    contract_status = models.CharField(
        'Status do Contrato',
        max_length=15,
        choices=ContractStatus.choices,
        default=ContractStatus.ACTIVE,
    )
    start_date = models.DateTimeField('Data de Início')
    end_date = models.DateTimeField('Data de Expiração')

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ('-start_date',)

    def __str__(self):
        return f'Contrato: {self.contract_number} -- {self.supplier.corporate_name}'
