from rest_framework import permissions

from .permissions import IsStaffEditorPermission


# This is included in all class based views to avoid repeating the permission classes
class StaffEditorPermissionMixin:
    permission_classes = [IsStaffEditorPermission, permissions.IsAdminUser]


# This can be used for other purposes such as queryset, serializer_class, lookup_field
# Standarization
