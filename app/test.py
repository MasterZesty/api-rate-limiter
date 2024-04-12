import requests
import time
import matplotlib.pyplot as plt

url = "http://127.0.0.1:5000"

response_codes = []
timestamps = []

# Specify the time interval and maximum number of requests
time_interval = 1  # in seconds
max_requests = 10

start_time = time.time()
num_requests = 0  # Initialize the request counter

while True:
    # Check if time interval has elapsed and reset the request counter
    if time.time() - start_time >= time_interval:
        start_time = time.time()
        num_requests = 0

    # Check if the maximum number of requests for the current interval has been reached
    if num_requests < max_requests:
        response = requests.request("GET", url)
        response_code = response.status_code
        response_codes.append(response_code)
        timestamps.append(time.time())
        print(f"Response Code: {response_code}")
        num_requests += 1

    # Assign colors based on response code
    colors = ['green' if code == 200 else 'red' if code == 429 else 'blue' for code in response_codes]

    # Plot the graph
    plt.clf()  # Clear the previous plot
    plt.scatter(timestamps, response_codes, c=colors)
    plt.yticks([200, 429])  # Set y-axis ticks to only include 200 and 429
    plt.xlabel('Time')
    plt.ylabel('Response Code')
    plt.title('Response Codes over Time')
    plt.grid(True)
    plt.pause(0.1)
