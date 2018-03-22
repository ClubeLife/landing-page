from django.contrib import admin
from django.urls import path

import landing.core.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index')
]
