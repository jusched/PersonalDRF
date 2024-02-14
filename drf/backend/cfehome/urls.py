from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # Local
    path("api/", include("api.urls")),
    path("api/products/", include("products.urls")),
    path("api/v2/", include("cfehome.routers")),
]
