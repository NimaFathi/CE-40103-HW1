import logging
from collections import OrderedDict

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from _helpers import set_logger
from account_management.models import Account

logger = set_logger(logging, __name__)


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'name',
        )
        writable_fields = ('name',)
        return_fields = ('name', 'username')

    def update(self, instance, validated_data):
        with transaction.atomic():
            try:
                for field in self.Meta.writable_fields:
                    if field in validated_data:
                        setattr(instance, field, validated_data[field])
                instance.save()
            except ValidationError as e:
                logger.error(e)
            return super(AccountUpdateSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        ret = OrderedDict()
        for field in self.Meta.return_fields:
            ret[field] = getattr(instance, field)
        return ret
