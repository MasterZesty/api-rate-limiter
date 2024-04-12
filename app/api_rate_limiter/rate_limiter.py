""""rate limiter"""

from functools import wraps
from flask import jsonify

class RateLimitExceededError(Exception):
    """Custom exception for API rate limit exceeded"""

    def __init__(self, message="API rate limit exceeded, send request after some time"):
        self.message = message
        super().__init__(self.message)

def rate_limiter(pool = None,
                        max_tokens: int = 10, refill_time: int = 1, refill_amount: int = 10,
                        limit_by_user: bool = False):
    """api rate limiter decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bucket_id = "534f8aed-88de-4a81-aa26-a3b0ed5da26a"
            if limit_by_user:
                bucket_id = kwargs.get('user_id', None)

            # Check if bucket exists, if not, create it
            if not pool.is_token_bucekt_exists(bucket_id):
                bkt_id, bucket = pool.create_token_bucket(bucket_id, max_tokens, \
                                                            refill_time, refill_amount, max_tokens)
                pool.add_bucket_in_pool(bkt_id, bucket)

            # Try to serve request
            if pool.bucket_pool[bucket_id].consume_token():
                return func(*args, **kwargs)

            # raise RateLimitExceededError()
            # If rate limit exceeded, raise HTTP 429 Too Many Requests error
            return jsonify({'error': 'API rate limit exceeded', 'message': f'Send request after {refill_time} seconds'}), 429


        return wrapper

    return decorator

