import json
import requests
from requests_oauthlib import OAuth1

api_key = "RAxZJEaWAk9dN54EhMoaWQLmk"
api_secret = "5220q5M9JRpiWGPhnWvhQcRP75Vf36UborGBtrV7US9FiCnMWk"
access_token_key = "726275714-LdcIFgeFXMXdECMG3Kpv7bbUIKJAZ7JDjwiMFa4o"
access_token_secret = "d6LL0lyxPVMfVzYZy88vSHOoOOahXjw6AgtutVqH4SlHL"

sent_file=open("AFINN-111.txt")
scores={}

for line in sent_file:
	l=[]
	l=line.split("\t")
	scores[l[0]]=int(l[1])
good=open("good.txt",'w')
bad=open("bad.txt",'w')


url = 'https://stream.twitter.com/1.1/statuses/filter.json?track=kejriwal'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)
try:
	r = requests.get(url, auth=auth, stream=True, timeout=10)
except Exception as e:
	print "some random exeption. try again"

cnt=10
# print type(r)
for line in r.iter_lines():

	if cnt==0:
		break
	if line:
		j=json.loads(line)
		print j['text']
		score=0
		l=[]
		l=j['text'].encode("utf8").split(" ")
		for word in l:
			if word in scores.keys():
				score=score + scores[word]
		print score
		if score>0:
			print "GOOD-SENTIMENT"
			good.write(j['text'].encode("utf8"))
		elif score<0:
			print "BAD-SENTIMENT"
			bad.write(j['text'].encode("utf8"))
		else:
			continue

		
   		
