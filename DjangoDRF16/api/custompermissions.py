from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True#only reead true all remaing crud false
        return False