
from cgitb import handler
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from login.views import *
from hr_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('hr/', include('hr_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404=pageNotFound
