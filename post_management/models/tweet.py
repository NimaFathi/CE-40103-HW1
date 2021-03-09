from django.db import models

from _helpers.db import TimeModel
from account_management.models import Account


class Tweet(TimeModel):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='نویسنده')
    context = models.CharField(max_length=250, verbose_name='متن', null=False, blank=False)

    class Meta:
        verbose_name = 'توییت'
        verbose_name_plural = 'توییت‌ها'
