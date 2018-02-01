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
        direction = float(self.request.get('direction'))
        move = CDBMove(direction=Direction(direction))
        move.put()
        self.response.out.write('saved move')

# request routing
application = webapp2.WSGIApplication([
                                    ('/', Draw),
                                    ], debug=True)
