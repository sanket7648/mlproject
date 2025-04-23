from functools import lru_cache
import time

class Cache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            self.cache.pop(next(iter(self.cache)))  # Remove the oldest item
        self.cache[key] = value

cache = Cache()

def cache_recommendations(user_id, recommendations):
    cache.set(user_id, recommendations)

def get_cached_recommendations(user_id):
    return cache.get(user_id)

def cache_with_expiry(user_id, recommendations, expiry_time):
    cache.set(user_id, (recommendations, time.time() + expiry_time))

def get_cached_recommendations_with_expiry(user_id):
    cached_data = cache.get(user_id)
    if cached_data:
        recommendations, expiry_time = cached_data
        if time.time() < expiry_time:
            return recommendations
        else:
            cache.set(user_id, None)  # Clear expired cache
    return None