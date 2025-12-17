#!/usr/bin/env python3
import serial
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# Initialize serial connection
ser = None

# Dictionary of pins with name of pin and state ON/OFF
pins = {
    2: {'name': 'PIN 2', 'state': 0},
    3: {'name': 'PIN 3', 'state': 0}
}

class LEDControlHandler(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        print(f"{self.address_string()} - {format % args}")
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
        
        # Root path - show dashboard
        if self.path == '/' or self.path == '':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.generate_html().encode())
            return
        
        # Handle toggle commands: /pin/action (e.g., /2/on or /3/off)
        if len(path_parts) == 2:
            try:
                pin = int(path_parts[0])
                action = path_parts[1]
                
                if pin in pins and action in ['on', 'off']:
                    self.handle_pin_control(pin, action)
                    self.send_response(302)
                    self.send_header('Location', '/')
                    self.end_headers()
                    return
            except ValueError:
                pass
        
        # Handle simple action commands: /action1, /action2, etc.
        if len(path_parts) == 1:
            action = path_parts[0]
            if action == 'action1':
                ser.write(b"1")
                pins[2]['state'] = 1
            elif action == 'action2':
                ser.write(b"2")
                pins[2]['state'] = 0
            elif action == 'action3':
                ser.write(b"3")
                pins[3]['state'] = 1
            elif action == 'action4':
                ser.write(b"4")
                pins[3]['state'] = 0
            else:
                self.send_response(404)
                self.end_headers()
                return
            
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
            return
        
        # 404 for unknown paths
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>404 - Not Found</h1>")
    
    def handle_pin_control(self, pin, action):
        """Control the LED pins"""
        if action == 'on':
            if pin == 2:
                ser.write(b"1")
                pins[pin]['state'] = 1
            elif pin == 3:
                ser.write(b"3")
                pins[pin]['state'] = 1
        elif action == 'off':
            if pin == 2:
                ser.write(b"2")
                pins[pin]['state'] = 0
            elif pin == 3:
                ser.write(b"4")
                pins[pin]['state'] = 0
    
    def generate_html(self):
        """Generate HTML dashboard"""
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control</title>
</head>
<body>
    <h1>LED Control Dashboard</h1>
    <p>Control your Arduino LEDs remotely</p>
    <hr>
"""
        
        # Generate LED sections dynamically
        for pin_num, pin_data in pins.items():
            state = pin_data['state']
            status_text = 'ON' if state == 1 else 'OFF'
            
            html += f"""
    <h2>{pin_data['name']} - Status: {status_text}</h2>
    <a href="/{pin_num}/on"><button>Turn ON</button></a>
    <a href="/{pin_num}/off"><button>Turn OFF</button></a>
    <br><br>
"""
        
        html += """
    <hr>
    <p><small>Powered by Python HTTP Server & Arduino</small></p>
</body>
</html>"""
        
        return html


def run_server(host='0.0.0.0', port=5000):
    """Start the HTTP server"""
    global ser
    
    # Initialize serial connection
    try:
        ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
        ser.flush()
        print(f"Serial connection established on /dev/ttyS0")
    except Exception as e:
        print(f"Warning: Could not open serial port: {e}")
        print("Server will start but LED control will not work")
    
    # Create and start server
    server_address = (host, port)
    httpd = HTTPServer(server_address, LEDControlHandler)
    
    print(f"Server running on http://{host}:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        if ser:
            ser.close()
        httpd.shutdown()
        print("Server stopped")


if __name__ == '__main__':
    run_server()
