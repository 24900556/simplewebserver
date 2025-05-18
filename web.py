from http.server import HTTPServer, BaseHTTPRequestHandler
content ="""
<html>
<title>Top Smartphone Manufacturers</title>
<body>
<table border="2" cellspacing="10" cellpadding="6">
<tr>
<th>S.No</th>
<th>Company</th>
<th>Market Share (%)</th>
</tr>
<tr>
<td>1</td>
<td>Samsung</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>Apple</td>
<td>18.8</td>
</tr>
<tr>
<td>3</td>
<td>Xiaomi</td>
<td>12.7</td>
</tr>
<tr>
<td>4</td>
<td>Oppo</td>
<td>8.6</td>
</tr>
<tr>
<td>5</td>
<td>Vivo</td>
<td>7.5</td>
</tr>
</table>
</body>
</html>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address =('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()