from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewset


router = DefaultRouter()
# First param: URL prefix (localhost:8000/api/v2/*products*/)
router.register(r"products", ProductViewset, basename="product")

urlpatterns = router.urls
