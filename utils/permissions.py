from rest_framework.permissions import BasePermission


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return request.user.is_authenticated and request.user.is_manager
        return True
