from django.conf.urls import include
from django.urls import path

from simplemooc.core.views import home, contact


app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]