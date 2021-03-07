import logging
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from _helpers import set_logger
from account_management.models import Account

logger = set_logger(logging, __name__)


class AccountLogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'name',
        )

    def to_representation(self, instance):
        ret = OrderedDict()
        for field in self.Meta.fields:
            ret[field] = getattr(instance, field)
        try:
            token = Token.objects.get(user=instance)
            ret['token'] = token.key
        except Token.DoesNotExist as e:
            logger.error(e)
        return ret
