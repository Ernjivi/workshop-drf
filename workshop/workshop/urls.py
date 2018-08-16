from django.contrib import admin
from django.urls import path, include

from domains import urls as domains_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(domains_urls)),
]
