import random
import string

from django.conf import settings
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
    tax_id = models.CharField('cpf', max_length=14, unique=True)
    phone = models.CharField('telefone', max_length=32)
    zipcode = models.CharField('cep', max_length=32)
    member_code = models.CharField('código de membro', max_length=32, unique=True)
    by_campaign = models.ForeignKey(
        'Campaign',
        related_name='conversions',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )

    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Associado'
        verbose_name_plural = 'Associados'

    @property
    def invite_url(self):
        return 'http://clube.life/signup/{}/'.format(self.member_code)

    def save(self, *args, **kwargs):
        if not self.id or not self.member_code:
            self.member_code = ''.join(
                random.choices(string.ascii_letters, k=settings.MEMBER_CODE_LENGTH)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class Campaign(models.Model):
    owner = models.ForeignKey('Associate', related_name='campaigns', on_delete=models.CASCADE)
    name = models.CharField('nome', unique=True, max_length=64)
    impressions = models.IntegerField('impressões', default=0)

    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'

    def __str__(self):
        return '{} - {}'.format(self.owner.user.email, self.name)
