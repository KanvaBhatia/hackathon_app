from rest_framework import permissions

class IsAuthorizedToAddHackathons(permissions.BasePermission):
    """
    Custom permission to only allow authorized users to add hackathons.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
