import re
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check is user is trying to update their own  profile"""
        if request.method in permissions.SAFE_METHODS: return True
        return obj.id == request.user.id
    
class UpdateOwnToDoItem(permissions.BasePermission):
    """Allow users to update their own to-do item"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their to-do item"""
        if request.method in permissions.SAFE_METHODS: return True
        return obj.user_profile.id == request.user.id