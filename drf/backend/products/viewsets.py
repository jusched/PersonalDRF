from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    """
    Get -> List -> Queryset
    Get -> Detail -> Product Instance Detail View
    Post -> Create -> New insance
    Put -> Update
    Patch -> Partial Update
    Delete -> Delete
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
