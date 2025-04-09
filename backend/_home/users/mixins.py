from users.permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    # classes order is important
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]