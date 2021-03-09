import logging

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from typing import Optional
from post_management.serializers import ListCommentSerializer
from post_management.models import Comment
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


class ListCommentView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    serializer_class = ListCommentSerializer
    pagination_class = LimitOffsetPagination

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[Comment]

    def get_queryset(self):
        return Comment.objects.filter(owner=self.request.user)
