from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url as r

from landing.core.forms import SignupForm, CampaignSignupForm
from landing.core.models import Associate, Campaign
from landing.core.utils import send_email


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})


def soon(request):
    return render(request, 'soon.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def politica(request):
    return render(request, 'politica.html', {})


def signup(request, member_code=None):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Getting user data
            user_fields = ['username', 'password', 'email', 'first_name', 'last_name']
            user_data = {k: data[k] for k in user_fields}
            associate_data = {k: data[k] for k in data if k not in user_fields}

            inviter_email = associate_data['inviter_email']
            del associate_data['inviter_email']
            inviter = User.objects.get(email=inviter_email).associate

            u = User.objects.create_user(**user_data)
            a = Associate.objects.create(user=u, influenced_by=inviter, **associate_data)

            send_email(a, 'Bem-vindo(a) ao Clube Life!', 'email/welcome.html')
            return redirect(r('soon'))
    else:
        form = SignupForm()
        if member_code is not None:
            a = Associate.objects.get(member_code=member_code)
            form = SignupForm(initial={'inviter_email': a.user.email})

    return render(request, 'signup.html', {'form': form})


def campaign(request, campaign_name):
    if request.method == 'POST':
        form = CampaignSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Getting user data
            user_fields = ['username', 'password', 'email', 'first_name', 'last_name']
            user_data = {k: data[k] for k in user_fields}
            associate_data = {k: data[k] for k in data if k not in user_fields}

            del associate_data['campaign_name']
            inviter = Associate.objects.get(campaigns__name='#' + campaign_name)

            u = User.objects.create_user(**user_data)
            a = Associate.objects.create(user=u, influenced_by=inviter, **associate_data)

            send_email(a, 'Bem-vindo(a) ao Clube Life!', 'email/welcome.html')
            return redirect(r('soon'))
    else:
        c = Campaign.objects.get(name='#' + campaign_name)
        c.impressions += 1
        c.save()
        form = CampaignSignupForm(initial={'campaign_name': '#' + campaign_name})

    return render(request, 'campaign.html', {
        'form': form,
        'campaign_name': campaign_name
    })
