from rest_framework import serializers

from post_management.models import Comment


class ListCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'owner',
            'context',
            'post'
        )
        read_only_fields = ('id', 'owner','post')
