from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from simplemooc.accounts.views import register, dashboard, edit, edit_password


app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('cadastre-se/', register, name='register'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]

