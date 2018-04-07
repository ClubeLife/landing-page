from django.contrib import admin
from django.urls import path, re_path

import landing.core.views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('dashboard', core_views.dashboard, name='dashboard'),
    path('login', core_views.login, name='login'),
    path('signup', core_views.signup, name='signup'),
    re_path('signup/(?P<member_code>.+)/$', core_views.signup, name='signup-user-code'),
    re_path('campaign/(?P<campaign_name>.+)/$', core_views.campaign, name='signup-campaign'),
    path('soon', core_views.soon, name='soon'),
    path('contact', core_views.contact, name='contact'),
    path('politica', core_views.politica, name='politica'),
    path('soon', core_views.soon, name='soon'),
]
