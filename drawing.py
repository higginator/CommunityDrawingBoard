import webapp2
import jinja2
import os

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

# request routing
application = webapp2.WSGIApplication([
                                    ('/', Draw)
                                    ], debug=True)
