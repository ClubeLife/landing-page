from django import forms

from landing.core import models


def inviter_email_validator(inviter_email):
    if not models.Associate.objects.filter(user__email=inviter_email).exists():
        raise forms.ValidationError('O e-mail de anfitrião especificado ainda não foi cadastrado.')


def associate_email_validator(email):
    if models.Associate.objects.filter(user__email=email).exists():
        raise forms.ValidationError('Este e-mail já foi cadastrado.')


class SignupForm(forms.Form):
    first_name = forms.CharField(label='Primeiro Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    date_of_birth = forms.DateField(
        label='Data de Nascimento', input_formats=['%d/%m/%Y']
    )
    tax_id = forms.CharField(label='CPF', max_length=20)
    phone = forms.CharField(label='Telefone', max_length=100)
    zipcode = forms.CharField(label='CEP', max_length=10)
    email = forms.EmailField(
        label='E-mail', max_length=255, validators=[associate_email_validator]
    )

    username = forms.CharField(label='Usuário', max_length=32)
    password = forms.CharField(label='Senha', max_length=100)

    inviter_email = forms.EmailField(
        label='E-mail de quem te convidou',
        required=False, max_length=255,
        validators=[inviter_email_validator]
    )
