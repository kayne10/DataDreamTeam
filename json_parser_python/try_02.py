import json
import unicodedata

#json_data=open('sample_json.json').read()
json_data=open('test.json').read()

data = json.loads(json_data)

#print data
#print len(data["results"])

#if "results" in data:
	#print data["results"]["title"]
	#print data["results"][1]['body']
	#for i in 
twits = []
for i in range(0, len(data["results"])):
#for i in range(0, 1):
	#print data["results"][i]['id']
	userName = (data["results"][i]['actor']['preferredUsername']).encode('utf8')
	date = (data["results"][i]['postedTime'][0:10]).encode('utf8')
	twit = (data["results"][i]['body']).encode('utf8')
	if 'geo' in data["results"][i]:
		lat = data["results"][i]['geo']['coordinates'][0]
		log = data["results"][i]['geo']['coordinates'][1]
		if lat < 0:
			lat = data["results"][i]['geo']['coordinates'][1]
			log = data["results"][i]['geo']['coordinates'][0]
	tp = (userName, date, lat, log, twit)
	twits.append(tp)
	
for i in twits:
	print i
