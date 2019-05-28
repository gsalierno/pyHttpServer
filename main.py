#!/usr/bin/python
from http.server import HTTPServer
from server import ReqHandler
import time

HOST_NAME	= 'localhost'
PORT_NUMBER = 8080

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME,PORT_NUMBER),ReqHandler)
    print(time.asctime(),'Server UP - %s:%s' % (HOST_NAME,PORT_NUMBER))
    try:
    	httpd.serve_forever()
    except KeyboardInterrput:
    	pass
    httpd.server_close()
    print(time.asctime(),'Server DOWN - %s:%s' % (HOST_NAME,PORT_NUMBER))
