from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('', include('simplemooc.core.urls', namespace='core')),
    path('cursos/', include('simplemooc.courses.urls', namespace='courses')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)