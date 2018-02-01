import webapp2

class Draw(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('drawing')

application = webapp2.WSGIApplication([
                                    ('/', Draw)
                                    ], debug=True)
