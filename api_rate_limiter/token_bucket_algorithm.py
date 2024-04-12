"""
tokn bucket algorithem
for api rate limting
"""

from datetime import datetime
from time import sleep

class TokenBucket():
    """
    TokenBucket
    """

    def __init__(self, bucket_id:str, max_tokens:int, refill_time:int,
                    refill_amount:int, value:int,
                    last_update:datetime, created_at:datetime) -> None:
        self.bucket_id =  bucket_id # a unique byte string that identifies the bucket
        self.max_tokens = max_tokens # the maximum number of tokens the bucket can hold
        self.refill_time = refill_time # the amount of time between refills
        self.refill_amount =  refill_amount # the no of tokens added to the bucket during a refill
        self.value = value # the current number of tokens in the bucket
        self.last_update = last_update # the last time the bucket was updated
        self.created_at = created_at # creation time of bucket

    def __str__(self):
        return f"bucket_id : {self.bucket_id}, value : {self.value}, \
                    last_update : {self.last_update}"

    def _add_token(self) -> None:
        """add token to bucket"""
        now = datetime.now()
        time_delta =  now - self.last_update

        if time_delta.total_seconds() >= self.refill_time:
            self.value = min(self.max_tokens, self.value + self.refill_amount)
            self.last_update = datetime.now()

    def consume_token(self) -> bool:
        """consume tokens in bucekt"""
        self._add_token()
        if self.value > 0:
            self.value -= 1
            return True

        return False


class TokenBucketManager():
    """
    TokenBucketManager
    """

    def __init__(self) -> None:
        self.bucket_pool = {}

    def create_token_bucket(self, bucket_id:str, max_tokens:int, refill_time:int,
                                refill_amount:int, value:int) -> tuple[str, TokenBucket]:
        """
        create token bucket
        """
        token_bucket = TokenBucket(bucket_id=bucket_id,
                                    max_tokens=max_tokens,
                                    refill_time=refill_time,
                                    refill_amount=refill_amount,
                                    value=value,
                                    last_update=datetime.now(),
                                    created_at=datetime.now())

        return bucket_id, token_bucket

    def is_token_bucekt_exists(self, bucket_id:str) -> bool:
        """
        check if bucket exist in pool
        """
        if self.bucket_pool.get(bucket_id, None):
            return True

        return False

    def add_bucket_in_pool(self, bucekt_id:str, token_bucket:TokenBucket) -> None:
        """
        add bucket in pool
        """
        self.bucket_pool[bucekt_id] = token_bucket

    def delete_bucket_from_pool(self, bucket_id:str) -> TokenBucket | None:
        """
        delete token bucekt
        """
        return self.bucket_pool.pop(bucket_id, None)


if __name__ == "__main__":
    print("token bucket rate limiting started!")
    
    n = 100
    user_id = "534f8aed-88de-4a81-aa26-a3b0ed5da26a"
    bucket_id=user_id
    max_tokens=10 # max number of tokens
    refill_time=60 # refill time in sec
    refill_amount=1 # number of token to add during refill
    t = 0 # time in sec between two request

    pool = TokenBucketManager()

    # if bucket not exist create it for user
    if not pool.is_token_bucekt_exists(bucket_id):
        bkt_id, bucket = \
        pool.create_token_bucket(bucket_id, max_tokens, refill_time, refill_amount, max_tokens)
        pool.add_bucket_in_pool(bkt_id, bucket)

    # simulate request from user
    for i in range(1,n):
        print(f"sending {i}th request from user {bucket_id}")

        # try to serve request
        if pool.bucket_pool[bucket_id].consume_token():
            print(f"{i}th request served returning response from server")
        else:
            print(f"rate limiting in action, send request after {t} seconds")

        sleep(t)
        
    print("token bucket rate limiting stopped!")