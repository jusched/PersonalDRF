from urllib import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, permissions

from django.shortcuts import get_object_or_404

from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin
from .models import Product
from .serializers import ProductSerializer


# Permission classes no longer needed to be declared inside APIViews
# StaffEditorPermissionMixin is a custom mixin that contains the permissions
class ProductListCreateAPIView(
    UserQuerysetMixin, StaffEditorPermissionMixin, generics.ListAPIView
):
    # IsAuthenticatedOrReadOnly allows unauthenticated users to read
    # Also, order matters. First verify if the user is admin then if he can edit
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] *
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        content = serializer.validated_data["description"] or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return qs.none()
    #     return qs.filter(user=request.user)


class ProductCreateAPIView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        content = serializer.validated_data["description"]
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(
    UserQuerysetMixin, StaffEditorPermissionMixin, generics.RetrieveAPIView
):
    # Automatically uses the ID of the model to retrieve the object
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(
    UserQuerysetMixin, StaffEditorPermissionMixin, generics.UpdateAPIView
):
    # Automatically uses the ID of the model to retrieve the object
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title
            instance.save()


class ProductDeleteAPIView(
    UserQuerysetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView
):
    # Automatically uses the ID of the model to retrieve the object
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# * This is the alternative way to create the views
@api_view(["GET", "POST", "PUT", "DELETE"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # * Detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)

        # * List view
        qs = Product.objects.all()
        data = ProductSerializer().data
        return Response(data)

    # * Create view
    elif method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data["title"]
            content = serializer.validated_data["description"]
            if content is None:
                content = title
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # * Update view
    elif method == "PUT":
        pass

    # * Delete view
    elif method == "DELETE":
        pass
