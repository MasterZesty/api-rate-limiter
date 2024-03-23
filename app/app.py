from flask import Flask
from utils import generate_city_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = generate_city_data()
    return data