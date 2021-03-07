import logging
from typing import Optional

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from account_management.models import Account

logger = logging.getLogger(__name__)


class LogInView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        context = {}
        username = request.data.get('username')
        password = request.data.get('password')
        account = authenticate(username=username, password=password)  # type: Optional[Account]
        logger.info(msg='user with username:{} tried to logged in'.format(username))
        if account:
            token, created = Token.objects.get_or_create(user=account)
            context['token'] = token.key
            context['response'] = 'successfully logged in'
            return Response(data=context, status=status.HTTP_200_OK)
        return Response(data={'response': 'username or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
