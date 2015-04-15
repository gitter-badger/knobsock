
import webapp2

class Home(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Knobsock in this bish')


app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)