import json
import unicodedata

# lets try to loop all gnip json files
json_data = open('file_01.json').readlines()
json_format = open('../Website/seeds/map.json', 'w')
json_geo_format_google_map = open('google_map.json', 'w')

json_out ={}
features = []

Type = {}
Type["type"] = "FeatureCollection"
json_out.update(Type)

for lines in json_data:
	data = json.loads(lines)
	marker = {} # all feature of a marker saves here
	tp ={}
	tp["type"] = "Feature"
	marker.update(tp)
	# -----------------------------------------------
	# property dictionary
	prop = {}
	name = {}
	name["Name"] = data['actor']['preferredUsername'].encode('utf8')
	date = {}
	date["Date"] = data['object']['postedTime'][0:10].encode('utf8')
	body = {}
	body["body"] = data['body'].encode('utf8')
	prop["properties"] = name
	prop["properties"].update(date)
	prop["properties"].update(body)
	marker.update(prop)
	#------------------------------------------------
	# geometry dictionary
	geo = {}
	tp2 = {}
	tp2["type"] = "Point"
	long_lat = []
	coord = {}
	if 'profileLocations' in data['gnip']:
		lng = 0.0
		lat = 0.0
		for items in data['gnip']['profileLocations']:
			lng = float( items['geo']['coordinates'][0])
			lat = float (items['geo']['coordinates'][1])
			if lng > 0:
				lng = float( items['geo']['coordinates'][1])
				lat = float (items['geo']['coordinates'][0])
		long_lat.append(lng)
		long_lat.append(lat)
	else:
		long_lat.append(0)
		long_lat.append(0)

	coord["coordinates"]= long_lat
	geo["geometry"] = tp2
	geo["geometry"].update(coord)


	#marker.update(prop)
	marker.update(geo)
	if long_lat[0] != 0:
		features.append(marker)

json_out["features"] = features
#print json_out
js = json.dumps(json_out, indent=4)
print >> json_format, js
print >> json_geo_format_google_map, "eqfeed_callback("
print >> json_geo_format_google_map, js
print >> json_geo_format_google_map, ")"
json_format.close()
json_geo_format_google_map.close()
#print json_out
