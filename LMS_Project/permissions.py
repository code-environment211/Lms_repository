from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return None
        return obj.instuctor == request.user
    
    