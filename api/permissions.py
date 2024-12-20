from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to allow read-only access to everyone,
    but restrict write access to authenticated users only.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS are: GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class IsStaffOrReadOnly(BasePermission):

    """
    Custom permission to allow only staff users to create, update, or delete.
    Everyone can read (GET) products.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in SAFE_METHODS:
            return True  # Everyone can view
        return request.user and request.user.is_staff  # Only staff users can modify
    


class IsSuperUser(BasePermission):
    """
    Custom permission to allow access only to superusers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser



class IsStaffUser(BasePermission):
    """
    Custom permission to allow access only to staff users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
