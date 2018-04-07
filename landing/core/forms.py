from django import forms
from django.conf import settings

from landing.core import models


def inviter_email_validator(inviter_email):
    if not models.Associate.objects.filter(user__email=inviter_email).exists():
        raise forms.ValidationError('O e-mail de associado especificado não cadastrado.')


def associate_email_validator(email):
    if models.Associate.objects.filter(user__email=email).exists():
        raise forms.ValidationError('Este e-mail já foi cadastrado.')


def validate_cpf(cpf):
    if settings.DEBUG:
        return

    mask_first_digit = list(range(10, 1, -1))
    mask_second_digit = list(range(11, 1, -1))
    cpf_digits = [int(x) for x in cpf if x.isdigit()]

    first_digit = ((10 * sum([a * b for a, b in zip(cpf_digits, mask_first_digit)])) % 11) % 10
    second_digit = ((10 * sum([a * b for a, b in zip(cpf_digits, mask_second_digit)])) % 11) % 10

    ending = '{}{}'.format(first_digit, second_digit)
    if not cpf.endswith(ending) or len(set(cpf_digits)) == 1:
        raise forms.ValidationError('O CPF informado é invalido.')


class SignupForm(forms.Form):
    first_name = forms.CharField(label='Primeiro Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    date_of_birth = forms.DateField(
        label='Data de Nascimento', input_formats=['%d/%m/%Y']
    )
    tax_id = forms.CharField(label='CPF', max_length=20, validators=[validate_cpf])
    phone = forms.CharField(label='Telefone', max_length=100)
    zipcode = forms.CharField(label='CEP', max_length=10)
    email = forms.EmailField(
        label='E-mail', max_length=255, validators=[associate_email_validator]
    )

    username = forms.CharField(label='Usuário', max_length=32)
    password = forms.CharField(label='Senha', max_length=100)

    inviter_email = forms.EmailField(
        label='E-mail de quem te convidou',
        required=True, max_length=255,
        validators=[inviter_email_validator]
    )


class CampaignSignupForm(forms.Form):
    first_name = forms.CharField(label='Primeiro Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    date_of_birth = forms.DateField(
        label='Data de Nascimento', input_formats=['%d/%m/%Y']
    )
    tax_id = forms.CharField(label='CPF', max_length=20, validators=[validate_cpf])
    phone = forms.CharField(label='Telefone', max_length=100)
    zipcode = forms.CharField(label='CEP', max_length=10)
    email = forms.EmailField(
        label='E-mail', max_length=255, validators=[associate_email_validator]
    )

    username = forms.CharField(label='Usuário', max_length=32)
    password = forms.CharField(label='Senha', max_length=100)

    campaign_name = forms.CharField(
        label='Nome da campanha',
        required=True, max_length=255
    )

    def clean_campaign_name(self):
        return self.cleaned_data['campaign_name'][1:]
