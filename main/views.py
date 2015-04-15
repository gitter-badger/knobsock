
from google.appengine.api import users
import webapp2
from main import models

class Home(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write('<h1>Knobsock in this bish ' + user.email() + '</h1>')
		else:
			self.redirect(users.create_login_url(self.request.uri))


app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)