import hashlib

from django.core.cache import caches
from django_plus.time import MIN


class TweetCache(object):
    cache = caches['default']
    timeout = 30 * MIN
    key_template = 'TW:tweet:{hash}'

    def get_key(self, username: str, user_id: int) -> str:
        serialise = [str(username), str(user_id)]
        _hash = hashlib.md5("".join(serialise).encode('utf-8')).hexdigest()
        return self.key_template.format(hash=_hash)

    def get(self, username: str, user_id: int) -> dict:
        key = self.get_key(username, user_id)
        return self.cache.get(key=key)

    def set(self, username: str, user_id: int, value) -> None:
        key = self.get_key(username, user_id)
        if key is not None:
            self.cache.set(key=key, value=value, timeout=self.timeout)

    def delete(self, username: str, user_id: int) -> None:
        key = self.get_key(username=username, user_id=user_id)
        self.cache.delete(key)


tweet_cache_handler = TweetCache()
