import logging

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from _helpers import set_logger
from post_management.models import Comment

logger = set_logger(logging, __name__)


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'owner',
            'context',
            'post'
        )
        read_only_fields = ('id', 'owner',)

    def validate(self, attrs):
        context = attrs.get('context', None)
        post = attrs.get('post', None)
        if context is None or post is None:
            logger.warning("empty comment")
            raise serializers.ValidationError({'error': 'comment could not be empty'})
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            try:
                create_data = {
                    'owner': self.context['data'].get('user'),
                    'post': validated_data['post'],
                    'context': validated_data['context'],
                }
                comment = Comment.objects.create(**create_data)
            except ValidationError as e:
                logger.error('could not create comment due to error: {}'.format(e))
                raise serializers.ValidationError(*e)
        return comment
