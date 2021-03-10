from django.db import models

from _helpers.db import TimeModel
from post_management.models import Tweet
from account_management.models import Account


class Comment(TimeModel):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE, verbose_name='توییت')
    context = models.CharField(max_length=250, verbose_name='متن', null=False, blank=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='نویسنده')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت‌ها'
