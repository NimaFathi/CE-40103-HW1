import logging

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from _helpers import set_logger
from post_management.models import Tweet

logger = set_logger(logging, __name__)


class UpdateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = (
            'id',
            'owner',
            'context'
        )
        read_only_fields = ('id', 'owner',)
        writable_fields = ('context',)

    def validate(self, attrs):
        context = attrs.get('context', None)
        if context == '':
            raise serializers.ValidationError({'error': 'tweet could not be empty'})
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            try:
                for field in self.Meta.writable_fields:
                    if validated_data.get(field, None) is not None:
                        setattr(instance, field, validated_data[field])
                instance.save()
                super(UpdateTweetSerializer, self).update(instance, validated_data)
            except ValidationError as e:
                logger.error(e)
        return instance
