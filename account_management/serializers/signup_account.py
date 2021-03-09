import logging
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from _helpers import set_logger
from account_management.models import Account

logger = set_logger(logging, __name__)


class AccountSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'name',
            'password'
        )

    def create(self, validated_data):
        if Account.objects.filter(username=validated_data['username']):
            logger.error('error in creating user due to duplicate username')
            raise serializers.ValidationError(
                {'error':
                     'اکانت با این نام‌کاربری وجود دارد لطفا نام‌کاربری دیگری را انتخاب کنید'}
            )
        return Account.objects.create(
            **validated_data
        )

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self.Meta.fields
        for field in fields:
            ret[field] = getattr(instance, field)
        token, created = Token.objects.get_or_create(user=instance)
        ret['token'] = token.key
        logger.warning('new user with username: {} created'.format(getattr(instance, 'username')))
        return ret
