from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('onememos/', include('onememos.urls')),
    path("admin/", admin.site.urls),
]
