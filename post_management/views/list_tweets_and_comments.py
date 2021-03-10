import logging
from collections import defaultdict

from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from _helpers.caches import cache_for
from post_management.models import Comment, Tweet

logger = logging.getLogger(__name__)


class ListPostView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        data = self._get_objects()
        paginated_data = self.paginate_queryset(data)
        return Response(data=paginated_data)

    @staticmethod
    @cache_for(5 * 60)
    def _get_objects():
        data = []
        tweets = Tweet.objects.all().order_by('-modified')
        for tweet in tweets:
            tweet_dict = defaultdict()
            tweet_dict['tweet'] = {
                'id': tweet.id,
                'owner__username': tweet.owner.username,
                'context': tweet.context
            }
            comments_list = []
            comments = Comment.objects.filter(post=tweet).order_by('-modified')
            for comment in comments:
                comments_list.append({
                    'id': comment.id,
                    'owner__username': comment.owner.username,
                    'context': comment.context,
                })
            tweet_dict['comments'] = comments_list
            data.append(tweet_dict)
        return data
