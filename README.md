# EX01 Developing a Simple Webserver
## Date: 11.03.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler

content = 
```
<!DOCTYPE html>
<html>
    <body bgcolor="PINK">
        <pre><code>
<table border="5" cellpadding="22" align="center" bgcolor="cyan">
    <caption align="center">TOP SMARTPHONE MANUFACTURERS</caption>
    <tr bgcolor="blue">
        <th>S.NO</th><th>COMPANY</th><th>MARKET SHARE (%)</th>
    </tr>
    <tr>
        <td>1</td><td>Samsung</td><td>20.1</td>
    </tr>
    <tr>
        <td>2</td><td>Apple</td><td>18.8</td>
    </tr>
    <tr>
        <td>3</td><td>Xiaomi</td><td>12.7</td>
    </tr>
    <tr>
        <td>4</td><td>Oppo</td><td>8.6</td>
    </tr>
    <tr>
        <td>5</td><td>Vivo</td><td>7.5</td>
    </tr>
</table>
        </code></pre>
    </body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-05-18 080252-1.png>) 
![alt text](<Screenshot 2025-03-19 141538-1.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
