from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)

    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    # In the serializer, it gets renamed into my_discount
    def get_discount(self):
        return "%.2f" % (float(self.price) * 0.65)
