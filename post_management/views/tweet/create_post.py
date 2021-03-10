import logging

from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from post_management.serializers import CreateTweetSerializer
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class CreateTweetView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateTweetSerializer

    def get_serializer_context(self):
        ctx = super(CreateTweetView, self).get_serializer_context()
        data = {
            'user': self.request.user,
        }
        ctx.update(data=data)
        return ctx
