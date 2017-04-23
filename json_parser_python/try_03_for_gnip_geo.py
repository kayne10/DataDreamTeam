import json
import unicodedata

#json_data=open('sample_json.json').read()
json_data = open('file_01.json').readlines()

json_out ={}



for lines in json_data:
	data = json.loads(lines)
	print data['actor']['preferredUsername']
	print data['object']['postedTime'][0:10]
	if 'profileLocations' in data['gnip']:
		for items in data['gnip']['profileLocations']:
			print float( items['geo']['coordinates'][0] )
			print float (items['geo']['coordinates'][1])
	print data['body']

