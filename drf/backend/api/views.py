from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # Verifies that the data that is being sent to the endpoint,
    # Is the same as the one in the Product model
    serializer = ProductSerializer(data=request.data)
    # This checks the requirements of the Product model such as max_length, required...
    if serializer.is_valid(raise_exception=True):
        # Saves the instance of the Product model
        serializer.save()
        return Response(serializer.data)
    return Response({"mesage": "This is not a valid product"}, status=400)

    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
