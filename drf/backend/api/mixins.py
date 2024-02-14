from rest_framework import permissions

from .permissions import IsStaffEditorPermission


# This is included in all class based views to avoid repeating the permission classes
class StaffEditorPermissionMixin:
    permission_classes = [IsStaffEditorPermission, permissions.IsAdminUser]


# This can be used for other purposes such as queryset, serializer_class, lookup_field
# Standarization


# Mixin for the queryset to be filtered by the user
class UserQuerysetMixin:
    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
