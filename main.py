from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests
import os

ip = os.getenv("VM_IP")
BASE_URL = f"http://{ip}"


def get_data():
    response = requests.get(f'http://{ip}:2038/data')
    payload = json.loads(response.content)
    
    if response.status_code != 200:
        print(payload)
        return f"Request error: {response.status_code}"
    
    # Get the first attribute value without relying on its name
    first_key = next(iter(payload))  # Get the first key in the dictionary
    return payload[first_key]


# Define a request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response status
        self.send_response(200)
        
        # Set headers
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        data = get_data()

        # Create a JSON response
        response = {
            "data": data,
        }
        
        # Write the response body
        self.wfile.write(json.dumps(response).encode('utf-8'))

# Set server address and port
port = 2101
server_address = ('', port)

# Initialize and start server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serving JSON on port {port}")
httpd.serve_forever()
