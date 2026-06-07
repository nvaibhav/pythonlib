import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
  def get(self):

if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/",basicRequestHandler)
  ])