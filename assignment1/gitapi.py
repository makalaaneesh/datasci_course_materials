import json
import requests
from requests_oauthlib import OAuth1

api_key = "RAxZJEaWAk9dN54EhMoaWQLmk"
api_secret = "5220q5M9JRpiWGPhnWvhQcRP75Vf36UborGBtrV7US9FiCnMWk"
access_token_key = "726275714-LdcIFgeFXMXdECMG3Kpv7bbUIKJAZ7JDjwiMFa4o"
access_token_secret = "d6LL0lyxPVMfVzYZy88vSHOoOOahXjw6AgtutVqH4SlHL"


# url = 'https://stream.twitter.com/1/statuses/sample.json'
url="https://stream.twitter.com/1.1/statuses/firehose.json"
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth, stream=True, timeout=5)
for line in r.iter_lines():
	if line:
		print line