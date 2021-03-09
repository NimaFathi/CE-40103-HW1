import hashlib

from django.core.cache import cache
from redis.exceptions import ConnectionError
from collections import OrderedDict


# get the cache key for storage
def cache_get_key(*args, **kwargs) -> str:
    serialise = []
    for arg in args:
        serialise.append(str(arg))
    sorted_kwargs = OrderedDict(sorted(kwargs.items()))
    for key, arg in sorted_kwargs.items():
        serialise.append(str(key))
        serialise.append(str(arg))
    key = hashlib.md5("".join(serialise).encode('utf-8')).hexdigest()
    return key


# decorator for caching functions
def cache_for(time):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            key = cache_get_key(fn.__name__,*args, **kwargs)
            try:
                result = cache.get(key)
                if result is None:
                    result = fn(*args, **kwargs)
                    if not result:
                        return result
                    cache.set(key, result, time)
            except ConnectionError:
                result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorator
