from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from simplemooc.accounts.views import register

app_name = 'accounts'

urlpatterns = [
    #path('entrar/', LoginView, {'template_name': 'accounts/login.html'}, name='login'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('cadastre-se/', register, name='register'),
]