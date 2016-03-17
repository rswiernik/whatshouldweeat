import io
import sys
import json
from yelp.client import Client
from yelp.errors import InvalidParameter
from yelp.oauth1_authenticator import Oauth1Authenticator

with io.open('config_secret.json') as cred_file:
	creds = json.load(cred_file)
	auth = Oauth1Authenticator(**creds)
	client = Client(auth)

params = {
	'term': 'food',
	'lang': 'fr'
}

try:
	response = client.search('San Francisco')
except InvalidParameter as e:
	print "Client error: ", e.text
	exit(1)

print repr(response)
