import webapp2
import jinja2
import os

from models.helpers.Direction import *
from models.CDBMove import CDBMove

# setup HTML template loader
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd() + '/templates'))


class Draw(webapp2.RequestHandler):
    def get(self):
        # HTML template
        template = template_env.get_template('drawing.html')

        # variable
        context = {}

        # response
        self.response.out.write(template.render(context))

    def post(self):
        move = self.request.get('move')

class MakeMove(webapp2.RequestHandler):
    def get(self):
        move = CDBMove(direction=Direction.UP)
        move.put()
        self.response.out.write('save move')


# request routing
application = webapp2.WSGIApplication([
                                    ('/', Draw),
                                    ('/make_move', MakeMove)
                                    ], debug=True)
