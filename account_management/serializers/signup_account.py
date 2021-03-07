import logging
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from account_management.models import Account



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
            raise serializers.ValidationError(
                {'error':
                     'اکانت با این نام‌کاربری وجود دارد لطفا یک نام‌کاربری دیگر انتخاب کنید'}
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
        return ret
