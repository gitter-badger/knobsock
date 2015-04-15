from google.appengine.ext import ndb
from google.appengine.api import users

class Group(ndb.Model):
	name = ndb.StringProperty()
	members = ndb.StructuredProperty(users, repeated=true)
