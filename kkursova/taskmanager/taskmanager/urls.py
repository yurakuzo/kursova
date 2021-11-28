from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('create', include('main.urls')),
    path('quadratic/', include('quadratic.urls')),
    path('newton/', include('newton.urls')),
]
