from django.utils.translation import gettext as _
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.public.urls', namespace='public')),
    path('account/', include('apps.account.urls', namespace='account')),
    path('service/', include('apps.service.urls', namespace='service')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('program/', include('apps.program.urls', namespace='program')),
    path('operation/', include('apps.operation.urls', namespace='operation')),
    path('communication/', include('apps.communication.urls', namespace='communication')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler403 = 'apps.public.views.err_403_handler'
# handler404 = 'apps.public.views.err_404_handler'
# handler500 = 'apps.public.views.err_500_handler'


# Rename site header & title & index_title
admin.site.site_header = _("Site Management")
admin.site.index_title = _("Management Panel")
admin.site.site_title = _("Vala Clinic")
