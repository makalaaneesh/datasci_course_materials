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

url = 'https://stream.twitter.com/1/statuses/sample.json'
# url="https://stream.twitter.com/1.1/statuses/firehose.json"
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth, stream=True, timeout=5)
cnt=100
# print type(r)
cities={}
for line in r.iter_lines():

	if cnt==0:
		break
	if line:
		#print "printing"
		j=json.loads(line)
		if 'delete' in j.keys():
			# print "bypassing delete"
			continue
		else:
			if j['lang'] !='en':
				continue
			if not j['place']:
				# print "no place"
				continue
			if j['place']['country'].lower() !='united states':
				continue
			
			# elif '#manu' not in j['text'].lower():
			# 	continue
			else:
				# print type(line)
				# print type(r.iter_lines)
				#print j.keys()
				# print j['created_at'], " ", j['place'], j['geo']
				print j['text']
				print j['place']['name']
				c=j['place']['name'].encode("utf8")
				score=0
				l=[]
				l=j['text'].encode("utf8").split(" ")
				for word in l:
					if word.lower() in scores.keys():
						score=score + int(scores[word.lower()])
				if score>0:
					if c not in cities.keys():
						cities[c]=int(1)
					else:
						cities[c]=int(cities[c]+1)
				if score<0:
					if c not in cities.keys():
						cities[c]=int(-1)
					else:
						cities[c]=int(cities[c]-1)


				cnt=cnt-1
				print "\n"
		# print "\n"
		# print j['lang']
		# cnt=cnt-1	
   		# print json.loads(line)
   		
for x in cities:
	print x, cities[x]