from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('create', include('main.urls')),
    path('quadratic/', include('quadratic.urls')),
    path('newton/', include('newton.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
