from google.appengine.ext import ndb
from google.appengine.api import users

class Group(ndb.Model):
	name = ndb.StringProperty()
	members = ndb.UserProperty(repeated=True)

class Knob(ndb.Model):
	name = ndb.StringProperty()
	parent = ndb.StructuredProperty(Group)
	sock = ndb.BooleanProperty()
	timeout = ndb.DateTimeProperty()