from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated