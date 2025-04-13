from users.permissions import IsStaffEditorPermission, IsOwnerOrSuperuser, IsActiveUser
from rest_framework import permissions

class StaffEditorPermissionMixin():
    # classes order is important
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, IsOwnerOrSuperuser]

class ActiveUserPermissionMixin():
    permission_classes = [IsActiveUser]