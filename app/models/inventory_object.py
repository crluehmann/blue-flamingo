__author__ = 'Chef'

from ferris import BasicModel
from google.appengine.ext import ndb

class InventoryObject (BasicModel):
    isActive       = ndb.BooleanProperty()
    type           = ndb.StringProperty()
    item           = ndb.StringProperty()
    description    = ndb.TextProperty()
    salesTaxCode   = ndb.StringProperty()
    account        = ndb.StringProperty()
    cogsAccount    = ndb.StringProperty()
    assetAccount   = ndb.StringProperty()
    quantityOnHand = ndb.IntegerProperty()
    unitOfMeasure  = ndb.StringProperty()
    cost           = ndb.FloatProperty()
    price          = ndb.FloatProperty()
    reorderPoint   = ndb.IntegerProperty()
    mpn            = ndb.StringProperty()
    weightPerPiece = ndb.FloatProperty()
    taxAgency      = ndb.StringProperty()
    preferredVendor         = ndb.StringProperty()
    unitOfMeasureSet        = ndb.StringProperty()
    purchaseDescription     = ndb.TextProperty()
    accumulatedDepreciation = ndb.FloatProperty()
