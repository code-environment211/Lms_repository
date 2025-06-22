from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow safe methods for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow write permissions to the instructor
        return obj.teacher == request.user
