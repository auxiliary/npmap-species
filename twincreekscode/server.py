import socket_handler
import tornado.ioloop
import sys

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r'/websocket', socket_handler.WebSocketHandler)]
		settings = {}
		tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
	if len(sys.argv) != 1:
		print 'usage: server.py'
		exit(1)

	server = Application()
	server.listen(5678)
	tornado.ioloop.IOLoop.instance().start()
