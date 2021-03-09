import logging

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from post_management.serializers import CreateCommentSerializer
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class CreateCommentView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateCommentSerializer

    def get_serializer_context(self):

        ctx = super(CreateCommentView, self).get_serializer_context()
        data = {
            'user': self.request.user,
        }
        ctx.update(data=data)
        return ctx
