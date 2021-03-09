import logging
from typing import Optional

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from post_management.models import Tweet
from post_management.serializers import UpdateTweetSerializer

logger = logging.getLogger(__name__)


class UpdateDeleteTweetView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = UpdateTweetSerializer
    model = Tweet

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]
        return [permission() for permission in self.permission_classes]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[Tweet]

    def get_object(self):
        if self.instance is None:
            self.instance = super().get_object()
        return self.instance

    def get_queryset(self):
        print('here')
        return Tweet.objects.filter(owner=self.request.user)
