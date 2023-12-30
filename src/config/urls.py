from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.public.urls', namespace='public')),
    path('account/', include('apps.account.urls', namespace='account')),
    path('service/', include('apps.service.urls', namespace='service')),
    path('operation/', include('apps.operation.urls', namespace='operation')),
    path('communication/', include('apps.communication.urls', namespace='communication')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler403 = 'apps.public.views.err_403_handler'
# handler404 = 'apps.public.views.err_404_handler'
# handler500 = 'apps.public.views.err_500_handler'
