from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop

from models.helpers.Direction import *

class CDBMove(ndb.Model):
    direction = msgprop.EnumProperty(Direction, required=True, indexed=True)
