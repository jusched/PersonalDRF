from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view(), name="product-list"),
    path("<int:pk>", views.ProductMixinView.as_view(), name="product-detail"),
    path(
        "<int:pk>/update/", views.ProductUpdateAPIView.as_view(), name="product-update"
    ),
    path(
        "<int:pk>/delete/", views.ProductDeleteAPIView.as_view(), name="product-delete"
    ),
]
