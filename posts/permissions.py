from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Only the author of a post can update or delete it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
