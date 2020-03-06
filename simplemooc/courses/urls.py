from django.conf.urls import include
from django.urls import path

from simplemooc.courses.views import index, details

app_name = 'courses'

urlpatterns = [
    path('', index, name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    path('(?P<slug>[\w_-]+)/$', details, name='details'),
]