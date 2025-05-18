from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
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
