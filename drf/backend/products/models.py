from django.conf import settings
from django.db import models
from django.db.models import Q


User = settings.AUTH_USER_MODEL


class ProductQuerySet(models.QuerySet):
    # Custom queryset with only products that are public
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        # Search both title and description of a product
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        # Filter them
        qs = self.is_public().filter(lookup)
        if user is not None:
            # Then filter them again by user
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().is_public.filter(title__icontains=query)


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    # This method is called from the algolia index to check if the product is public
    def is_public(self) -> bool:
        return self.public

    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    # In the serializer, it gets renamed into my_discount
    def get_discount(self):
        return "%.2f" % (float(self.price) * 0.65)
