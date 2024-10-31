from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

BASE_URL = "http://192.168.100.11"


def get_data():
    response = requests.get(BASE_URL + ":2038/data")
    if response.status_code != 200:
        print(response.json())
        return f"Request error: {response.status_code}"
    return response.json().get("value")


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
