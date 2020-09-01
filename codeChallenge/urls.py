from django.contrib import admin
from django.urls import path, include
from apps import flattener

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.flattener.urls')),
]
