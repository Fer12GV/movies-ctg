from rest_framework.permissions import BasePermission
from unittest import TestCase


class IsAuthenticatedOrReadOnlyCustom(BasePermission):

    def has_permission(self, request, view):
        return request.method.lower() == 'get' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method.lower() == 'get' or request.user.is_authenticated
