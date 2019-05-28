#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
from routes import routes
from pathlib import Path

class ReqHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.respond()

	def do_POST(self):
		return

	def handle_http(self):
		status = 200
		content_type = "text/plain"
		response_content = ""

		if self.path in routes:
			print(routes[self.path])
			route_content = routes[self.path]
			filepath = Path('templates/{}'.format(route_content))
			print(filepath)
			if filepath.is_file():
				print("TEST")
				content_type = "text/html"
				response_content = open(filepath)
				response_content = response_content.read()
			else:
				response_content = "404 Not Found"
		else:
			content_type = "text/plain"
			response_content = "404 Not Found"
		self.send_response(status)
		self.send_header('Content-type',content_type)
		self.end_headers()
		return bytes(response_content,"UTF-8")


	def respond(self):
		content = self.handle_http()
		self.wfile.write(content)
