"""app"""

from flask import Flask, jsonify
from utils import generate_city_data
from api_rate_limiter.token_bucket_algorithm import TokenBucketManager
from api_rate_limiter.rate_limiter import rate_limiter


app = Flask(__name__)

pool = TokenBucketManager()

@app.route("/")
@rate_limiter(pool=pool, max_tokens=1, refill_time=10, refill_amount=1, limit_by_user=False)
def hello_world():
    """test endpoint"""
    data = generate_city_data()
    return jsonify(data), 200
