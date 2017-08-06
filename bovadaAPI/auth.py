import os
from error import BovadaException, BovadaAuthenticationError
from headers import get_bovada_headers_generic
import requests
import json
import time


def login_to_bovada(username, password):
	"""on purpose I kept the login flow the same as if you were logging into Bovada using a browser.
		I could have just queried the api/token endpoint directly, but figured that may raise some
		flags with bovada since the login process would be skipping a step.
	"""
	query_1 = query_login_endpoint() #query the login endpoint like we would if using a browser
	if query_1.status_code == 200:
		authenticated_ourselves = bovada_auth(username=username, password=password)
		if authenticated_ourselves.status_code == 200:
			return authenticated_ourselves
		else:
			raise BovadaAuthenticationError(authenticated_ourselves.reason)
	else:
		raise BovadaException(query_1.reason)



def query_login_endpoint():
	return requests.get("https://sports.bovada.lv/websites/services/components/login", headers=get_bovada_headers_generic())


#pass in a dictionary where username is the username of the account
#and password is the password to the account
def bovada_auth(username, password):
	cookies = {
    'JOINED': 'true',
    'BG_UA': 'Desktop|OS X|10_12_1|Chrome|55.0.2883.95||',
    'ux': 'created=true',
    'ln_grp': '2',
    'LANGUAGE': 'en',
    'ADRUM': 's=1483171346890&r=https%3A%2F%2Fwww.bovada.lv%2F%3F0',
    'has_js': '1',
    'DEFLANG': 'en',
    's_cc': 'true',
    'bsp': '1',
    's_fid': '25EB81C40CBC6670-086F7CF1DDF960B8',
    's_sq': 'bdbovadalv%3D%2526pid%253DbovadaLV%25253AHome%2526pidt%253D1%2526oid%253DLogin%2526oidt%253D3%2526ot%253DSUBMIT',
}
	print 'called'
	if not username and password:
		try:
			username = os.environ["BOVADA_USERNAME"]
		except KeyError:
			raise BovadaException("could not find your bovada username. Did you export it as an environment variable?")
		try:
			password = os.environ["BOVADA_PASSWORD"]
		except KeyError:
			raise BovadaException("Could not find your bovada password. Did you export it as an environment variable?")


	payload = json.dumps({
		"username": username,
		"password":password})
	return requests.post("https://sports.bovada.lv/services/web/v2/oauth/token",
		data=payload,
		cookies=cookies,
		headers=get_bovada_headers_generic())
