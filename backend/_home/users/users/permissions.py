from rest_framework.permissions import DjangoModelPermissions, BasePermission, SAFE_METHODS, AllowAny


class IsOwnerOrSuperuser(BasePermission):
    """
        custom permission to only allow owners of an object to edit it,
        or superuser to edit any object.
        """

    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_superuser

class IsStaffEditorPermission(DjangoModelPermissions):
    # using a custom permission so a staff that does not have permission can not view the product list
    # staff permissions are set in django admin page

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class IsActiveUser(BasePermission):
    """Allow only active users to perform actions."""
    message = "Your account is inactive. Please contact support."

    def has_permission(self, request, view):
        # Only allow if user is authenticated AND active
        return request.user and request.user.is_authenticated and request.user.is_active

# class IsActiveOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return AllowAny
#         else:
#             return request.user.is_active

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm('products.view_product'):
    #             return True
    #         if user.has_perm('products.add_product'):
    #             return True
    #         if user.has_perm('products.delete_product'):
    #             return True
    #         if user.has_perm('product.change_product'):
    #             return True
    #         return False
    #     return False
