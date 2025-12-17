#!/usr/bin/env python3
import pymysql
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from datetime import datetime

# Database configuration
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "rootpassword"
DB_NAME = "iot"

# Dictionary of pins with name of pin and state ON/OFF
pins = {
    2: {'name': 'PIN 2', 'state': 0},
    3: {'name': 'PIN 3', 'state': 0}
}


def get_db_connection():
    """Create and return database connection"""
    try:
        return pymysql.connect(host=DB_HOST, port=3306, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None


def log_led_state(pin, state, action):
    """Log LED state changes to database"""
    dbConn = get_db_connection()
    if dbConn:
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = (timestamp, pin, state, action)
            cursor = dbConn.cursor()
            cursor.execute(
                "INSERT INTO led_log (timestamp, pin, state, action) VALUES (%s, %s, %s, %s)",
                data
            )
            dbConn.commit()
            cursor.close()
        except Exception as e:
            print(f"Error logging to database: {e}")
        finally:
            dbConn.close()


def get_recent_logs(limit=10):
    """Retrieve recent LED state changes from database"""
    dbConn = get_db_connection()
    logs = []
    if dbConn:
        try:
            cursor = dbConn.cursor()
            cursor.execute(
                "SELECT timestamp, pin, state, action FROM led_log ORDER BY timestamp DESC LIMIT %s",
                (limit,)
            )
            logs = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(f"Error reading from database: {e}")
        finally:
            dbConn.close()
    return logs


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
        
        # 404 for unknown paths
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>404 - Not Found</h1>")
    
    def handle_pin_control(self, pin, action):
        """Control the LED pins and log to database"""
        if action == 'on':
            pins[pin]['state'] = 1
            log_led_state(pin, 1, 'on')
        elif action == 'off':
            pins[pin]['state'] = 0
            log_led_state(pin, 0, 'off')
    
    def generate_html(self):
        """Generate HTML dashboard with database logs"""
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control with Database</title>
</head>
<body>
    <h1>LED Control Dashboard</h1>
    <p>Control your Arduino LEDs remotely with database logging</p>
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
        
        # Add database log section
        html += """
    <hr>
    <h2>Recent Activity Log</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Timestamp</th>
            <th>Pin</th>
            <th>State</th>
            <th>Action</th>
        </tr>
"""
        
        # Fetch and display recent logs
        logs = get_recent_logs(10)
        if logs:
            for log in logs:
                timestamp, pin, state, action = log
                state_text = 'ON' if state == 1 else 'OFF'
                html += f"""
        <tr>
            <td>{timestamp}</td>
            <td>PIN {pin}</td>
            <td>{state_text}</td>
            <td>{action}</td>
        </tr>
"""
        else:
            html += """
        <tr>
            <td colspan="4">No logs available</td>
        </tr>
"""
        
        html += """
    </table>
    <br>
    <hr>
    <p><small>Powered by Python HTTP Server, Arduino & MySQL</small></p>
</body>
</html>"""
        
        return html


def init_database():
    """Initialize database table if it doesn't exist"""
    dbConn = get_db_connection()
    if dbConn:
        try:
            cursor = dbConn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS led_log (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    timestamp DATETIME NOT NULL,
                    pin INT NOT NULL,
                    state INT NOT NULL,
                    action VARCHAR(10) NOT NULL
                )
            """)
            dbConn.commit()
            cursor.close()
            print("Database table 'led_log' ready")
        except Exception as e:
            print(f"Error initializing database: {e}")
        finally:
            dbConn.close()


def run_server(host='0.0.0.0', port=5000):
    """Start the HTTP server"""
    # Create and start server
    server_address = (host, port)
    httpd = HTTPServer(server_address, LEDControlHandler)
    
    print(f"Server running on http://{host}:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
        print("Server stopped")


if __name__ == '__main__':
    run_server()
