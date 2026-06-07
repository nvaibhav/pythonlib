import tornado.web
import tornado.ioloop


class MyRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi from backend server")

class MyQueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        myquery = self.get_query_argument("myquery", default="empty")
        self.write(f"Query parameter received: {myquery}")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",MyRequestHandler),
        (r"/whatquery",MyQueryParamRequestHandler)
    ])
    try:
        app.listen(8882)
        print("Application has started listening")
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Application has stopped listening")