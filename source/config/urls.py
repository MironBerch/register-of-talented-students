from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('', include('reporting.urls')),
]


handler400 = 'core.views.bad_request'
handler403 = 'core.views.access_denied_error'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)