from time import sleep
from datetime import datetime


class TokenBucket():
    
    def __init__(self, bucket_id:str, max_tokens:int, refill_time:int, refill_amount:int, value:int, last_update:datetime, created_at:datetime):
        self.bucket_id =  bucket_id # a unique byte string that identifies the bucket
        self.max_tokens = max_tokens # the maximum number of tokens the bucket can hold
        self.refill_time = refill_time # the amount of time between refills
        self.refill_amount =  refill_amount # the number of tokens that are added to the bucket during a refill
        self.value = value # the current number of tokens in the bucket
        self.last_update = last_update # the last time the bucket was updated
        self.created_at = created_at # creation time of bucket

    def __str__(self):
        return f"bucket_id : {self.bucket_id}, max_tokens : {self.max_tokens}, \
                refill_time : {self.refill_time}, refill_amount: {self.refill_amount}, \
                value : {self.value}, last_update : {self.last_update}, created_at : {self.created_at}"



if __name__ == "__main__":
     print(f"token bucket rate limiting")
     N = 100
     user_id = "534f8aed-88de-4a81-aa26-a3b0ed5da26a"
     t = 1
     bucket = {}

     for i in range(N):
        print(f"sending {i}th request from user {user_id}")
        
        # check if bucket exist for given user or not
        if bucket.get(user_id, 0) == 0:
            bucket[user_id] = TokenBucket(user_id, 10, 1, 1, 10, datetime.now(), datetime.now())

        
        # check bucket is empty if empty invalid request
        if bucket.get(user_id).value <= 0:
            print(f"rate limiting in action all tokens are used please send request after {t} seconds")
            continue

        print(f"request served returning response from server")
        bucket.get(user_id).value -= 1
        bucket.get(user_id).last_update = datetime.now()
        
        print(bucket.get(user_id))

        sleep(t)
