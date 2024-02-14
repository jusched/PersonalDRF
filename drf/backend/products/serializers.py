from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    # This way, we can change the name of the get_discount method to my_discount
    my_discount = serializers.SerializerMethodField(read_only=True)
    related_products = ProductInlineSerializer(
        source="user.products_set.all", read_only=True, many=True
    )
    edit_url = serializers.SerializerMethodField(read_only=True)
    # Only works on a ModelSerializer
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    title = serializers.CharField(validators=[validators.validate_title])
    # email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Product
        # We add the method to the fields list
        fields = [
            "owner",
            # "email",
            "url",
            "edit_url",
            "id",
            "title",
            "description",
            "price",
            "sale_price",
            "my_discount",
            "related_products",
        ]

    # Then declare the method to be used from the Product model
    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            # This checks if the object is an instance of the Product model
            raise TypeError("This is not a valid product")
        return obj.get_discount()

    def get_edit_url(self, obj):
        request = self.context.get("request")
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)
