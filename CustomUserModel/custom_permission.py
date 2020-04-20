from rest_framework import permissions


class IsCreationOrIsAuthenticated(permissions.BasePermission):
    """
        Custom permission:
            - allow anonymous POST
            - allow authenticated GET and PUT on *own* record
            - allow all actions for staff
        """

    def has_permission(self, request, view):

        return view.action == 'create' or request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, current_user):
        return view.action in ['retrieve', 'update',
                               'partial_update'] and current_user.id == request.user.id or request.user.is_staff