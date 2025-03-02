from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("authentication.urls")),
    path('o/', include("owner.urls")),
    path('w/', include("worker.urls")),
]
