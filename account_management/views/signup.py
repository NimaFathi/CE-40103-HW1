import logging

from django_plus.api import UrlParam as _p
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from account_management.models import Account
from account_management.serializers import AccountLogInSerializer, AccountUpdateSerializer, AccountSignUpSerializer

logger = logging.getLogger(__name__)


class CreatAccountPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method == 'GET':  # create new user by anyone
            return True
        return bool(request.user and request.user.is_authenticated)


class AccountViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CreatAccountPermission,)
    list_params_template = [
        _p('username', _p.string)
    ]
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return AccountUpdateSerializer
        elif self.request.method == 'POST':
            return AccountSignUpSerializer
        return AccountLogInSerializer

    def get_queryset(self):
        _query = None
        if self.request.method == 'GET':
            username = _p.clean_data(self.request.query_params, self.list_params_template)['username']
            _query = Account.objects.filter(username=username)
        elif self.request.method == 'PATCH':
            username = self.kwargs['username']
            _query = Account.objects.filter(username=username)
        return _query
