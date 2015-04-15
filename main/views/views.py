
import webapp2

from google.appengine.api import users

class Home(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Knobsock in this bish ' + user.email())
		else:
			self.redirect(users.create_login_url(self.request.uri))


app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)