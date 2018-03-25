from django.contrib.auth.models import User
from django.db import models


class Associate(models.Model):
    user = models.OneToOneField(
        User,
        related_name='associate',
        on_delete=models.CASCADE
    )
    influenced_by = models.ForeignKey(
        'Associate',
        related_name='influenced',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField('data de nascimento')
    tax_id = models.CharField('cpf', max_length=14)
    phone = models.CharField('telefone', max_length=32)
    zipcode = models.CharField('cep', max_length=32)

    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Associado'
        verbose_name_plural = 'Associados'

    def __str__(self):
        return self.user.email
