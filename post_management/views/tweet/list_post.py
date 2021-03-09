import logging
from typing import Optional

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from _helpers.caches.tweet_cache import tweet_cache_handler
from post_management.models import Tweet
from post_management.serializers import ListTweetSerializer

logger = logging.getLogger(__name__)


class ListTweetView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated.)
    serializer_class = ListTweetSerializer
    pagination_class = LimitOffsetPagination

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[Tweet]

    def get_queryset(self):
        return Tweet.objects.filter(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        username = self.request.user.username
        user_id = self.request.user.id
        cached_value = tweet_cache_handler.get(username=username, user_id=user_id)
        if cached_value is not None:
            return Response(cached_value)

        res = super(ListTweetView, self).list(request, *args, **kwargs)
        tweet_cache_handler.set(username=username, user_id=user_id, value=res.data)
        return res
