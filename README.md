# API Rate Limiter

api rate limiter for flask app uses token bucket algorithm to limit the incoming request flow.

### rate limiting in action for max_tokens=1, refill_time=10, refill_amount=1, limit_by_user=False

![Rate Limiter](https://github.com/MasterZesty/api-rate-limiter/blob/main/docs/imgs/1request_10sec.png)
