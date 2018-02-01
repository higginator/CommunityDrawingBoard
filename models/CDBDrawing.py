from google.appengine.ext import ndb
from models.CDBMove import CDBMove

class CDBDrawing(ndb.Model):
    moves = ndb.KeyProperty(kind=CDBMove, repeated=True)
