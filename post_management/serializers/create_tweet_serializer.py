import logging

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from _helpers import set_logger
from post_management.models import Tweet

logger = set_logger(logging, __name__)


class CreateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = (
            'id',
            'owner',
            'context'
        )
        read_only_fields = ('id', 'owner',)

    def validate(self, attrs):
        context = attrs.get('context', '')
        logger.info('create tweet')
        if context == '':
            logger.warning("error: empty tweet")
            raise serializers.ValidationError({'error': 'tweet could not be empty'})
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            try:
                create_data = {
                    'owner': self.context['data'].get('user'),
                    'context': validated_data['context'],
                }
                tweet = Tweet.objects.create(**create_data)
            except ValidationError as e:
                logger.error(e)
                raise serializers.ValidationError(*e)
        return tweet
