from django.contrib import admin
from django.urls import path

import landing.core.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('login', core_views.login, name='login'),
    path('dashboard', core_views.dashboard, name='dashboard'),
    path('soon', core_views.soon, name='soon'),
    path('signup', core_views.signup, name='signup'),
]
