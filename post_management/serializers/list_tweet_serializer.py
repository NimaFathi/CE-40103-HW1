from rest_framework import serializers

from post_management.models import Tweet


class ListTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = (
            'id',
            'owner',
            'context'
        )
        read_only_fields = ('id', 'owner',)
