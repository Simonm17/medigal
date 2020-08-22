from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('index.urls')),
    path('contacts/', include('contacts.urls')),
    path('doctors/', include('doctors.urls')),
    path('applicants/', include('applicants.urls')),
    path('company/', include('company.urls')),
    path('scheduling/', include('scheduling.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
