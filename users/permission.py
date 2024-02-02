from rest_framework.permissions import BasePermission, SAFE_METHODS


class LoginRequired(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_anonymous) or (request.auth is None):
            return False
        result = True if request.user.social_id == request.auth.payload.get('social_id') else False
        return bool(result and request.user.role_id)

class AdminRequired(BasePermission):
    def has_permission(self, request, view):
        result = False
        if (request.user.is_anonymous) or (request.auth is None):
            return result
        elif request.user.social_id == request.auth.payload.get('social_id'):
            result = True if (request.user.is_admin and request.user.role_id == 1 ) else False
        return result

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.member_type == 'seller'
