import random
import threading
import time
from flask import Flask, request

# Define list of simulated servers
servers = [
  {"name": "Server 1", "host": "127.0.0.1", "port": 5001},
  {"name": "Server 2", "host": "127.0.0.1", "port": 5002},
  {"name": "Server 3", "host": "127.0.0.1", "port": 5003}
]

# Round-robin index for load balancing
index = 0

# Create function to simulate servers
def create_server(name, host, port):
  app = Flask(name)

  @app.route('/')
  def home():
    return f"Response from {name}"
  
  # Run each server in separate thread
  threading.Thread(target=lambda: app.run(host=host, port=port, debug=False)).start()
total_number_requests = 10

# Function to stimulate load balancer
def load_balancer():
  global index
  for i in range(total_number_requests):
    # Stimulate load balancer
    request_id = random.randint(1000, 9999)
    # Select next server in list usign round-robin
    server = servers[index]
    index = (index + 1) % len(servers)

  # Print assigned server for this report
  print(f"Request {request_id} is handled by {server['name']}")

  # Stimulate time between requests
  time.sleep(random.uniform(0.5, 2))

# Create simulated servers
for server in servers:
  create_server(server['name'], server['host'], server['port'])

# Start load balancer simulation in separate thread
threading.Thread(target=load_balancer).start()