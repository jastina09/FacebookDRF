from rest_framework.permissions import BasePermission

class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                request.user.user_type == 'shopping')

class CreatePostPermission(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                request.user.user_type == 'blog')