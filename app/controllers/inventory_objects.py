__author__ = 'Adam'

from ferris import Controller, scaffold
from ferris.components import oauth
from apiclient.discovery import build

class InventoryObjects(Controller):
    class Meta:
        prefixes     = ('viewer','editor',)
        components   = (scaffold.Scaffolding,oauth.OAuth) # This is how we OAuth2
        oauth_scopes = ['https://www.googleapis.com/auth/cloud-platform',
                        'https://www.googleapis.com/auth/datastore',
                        'https://www.googleapis.com/auth/userinfo.email']

#    @oauth.require_credentials
#    def list(self):
#        return "Nonsense from the controller goes here"

    list   = scaffold.list
    add    = scaffold.add
    edit   = scaffold.edit
    delete = scaffold.delete