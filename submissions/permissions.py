from rest_framework import permissions

# Custom permission to only allow authorized users to add hackathons.
class IsAuthorizedToAddHackathons(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
