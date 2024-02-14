from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # This way, we can change the name of the get_discount method to my_discount
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        # We add the method to the fields list
        fields = ["id", "title", "description", "price", "sale_price", "my_discount"]

    # Then declare the method to be used from the Product model
    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            # This checks if the object is an instance of the Product model
            raise TypeError("This is not a valid product")
        return obj.get_discount()
