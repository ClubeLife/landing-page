from django.contrib.auth.models import User
from django.db import models


class Associate(models.Model):
    user = models.OneToOneField(User, related_name='associate', on_delete=models.CASCADE)
    influenced_by = models.ForeignKey('Associate', related_name='influenced', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField('primeiro nome', max_length=128)
    last_name = models.CharField('sobrenome', max_length=128)
    tax_id = models.CharField('cpf', max_length=14)
    phone = models.CharField('telefone', max_length=32)

    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)
