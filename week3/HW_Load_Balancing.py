import random
import threading
import time
from flask import Flask, request

# Define a list of simulated servers
servers = [
    {"name": "Server 1", "host": "127.0.0.1", "port": 5001, "connections": 0, "weight": 7},
    {"name": "Server 2", "host": "127.0.0.1", "port": 5002, "connections": 0, "weight": 4},
    {"name": "Server 3", "host": "127.0.0.1", "port": 5003, "connections": 0, "weight": 1}
]

# Round-robin index for load balancing
index = 0
connections = 0

# Create a function to simulate servers
def create_server(name, host, port):
    app = Flask(name)

    @app.route('/')
    def home():
        return f"Response from {name}"

    # Run each server in a separate thread
    threading.Thread(target=lambda: app.run(host=host, port=port, debug=False)).start()
total_number_requests = 10

# Functions to simulate the load balancers
def round_robin_load_balancer():
    global index
    for i in range(total_number_requests):
        # Simulate an incoming request
        request_id = random.randint(1000, 9999)
        start = time.perf_counter()
        # Select the next server in the list using round-robin
        server = servers[index]
        index = (index + 1) % len(servers)
        # Print the assigned server for this request
        end = time.perf_counter()
        print(f"Request {request_id} is handled by Round Robin {server['name']} and took {end-start:.12f} seconds.")

        # Simulate time between requests
        time.sleep(random.uniform(0.5, 2))

def least_connections_load_balancer():
    global connections
    for i in range(total_number_requests):
        # Simulate an incoming request
        request_id = random.randint(1000, 9999)
        start = time.perf_counter()
        # Select the next server in the list using Least Connections
        server = min(servers, key=lambda server: server["connections"])
        server["connections"] += 1
        # Print the assigned server for this request
        end = time.perf_counter()
        # Algorithm should subtract current connection when done processing, but there is no random packet distributor in this code
        # and packets are processed one at a time for the legacy codebase. Lag time can be simulated into this code to illustrate the full picture. 
        # server = server["connections"] -=1
        print(f"Request {request_id} is handled by Least Connections {server['name']} and took {end-start:.12f} seconds.")

        # Simulate time between requests
        time.sleep(random.uniform(0.5, 2))

def weighted_distribution_load_balancer():
    global connections
    for i in range(total_number_requests):
        # Simulate an incoming request
        request_id = random.randint(1000, 9999)
        start = time.perf_counter()
        # Select the next server in the list using round-robin
        server = min(servers, key=lambda server: server["weight"] / server["weight"])
        server["connections"] += 1

        # Print the assigned server for this request
        end = time.perf_counter()
        print(f"Request {request_id} is handled by Weighted Distribution {server['name']} and took {end-start:.12f} seconds.")

        # Simulate time between requests
        time.sleep(random.uniform(0.5, 2))

# Create simulated servers
for server in servers:
    create_server(server['name'], server['host'], server['port'])

# Start the load balancer simulations in a separate thread
requestThread = threading.Thread(target=round_robin_load_balancer)
requestThread.start()
requestThread.join()

requestThread = threading.Thread(target=least_connections_load_balancer)
requestThread.start()
requestThread.join()

requestThread = threading.Thread(target=weighted_distribution_load_balancer)
requestThread.start()
requestThread.join()