from rest_framework import serializers

from .models import Product


# Can be on the model, inside the serializer or below the serializer as a function
def validate_title(self, value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError("This title has already been used")
    return value
