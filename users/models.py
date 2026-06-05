import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(
        'Identificador', primary_key=True, default=uuid.uuid4, editable=False
    )
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username
