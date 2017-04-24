import json
import unicodedata
import os


def json_output(input_file):

	features = []

	for lines in input_file:
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
	return features
	#json_out["features"] = features
	#return json_out


def main():
	json_out_1 = {}
	json_out_2 = {}
	json_out_3 = {}
	json_out_4 = {}
	features = []

	Type = {}
	Type["type"] = "FeatureCollection"
	json_out_1.update(Type)
	json_out_2.update(Type)
	json_out_3.update(Type)
	json_out_4.update(Type)


	
	path_read 	= 	'/root/DataDreamTeam/shineynewset/'
	
	one_json_1 = open('one_json_1.json', 'w')
	one_json_2 = open('one_json_2.json', 'w')
	one_json_3 = open('one_json_3.json', 'w')
	one_json_4 = open('one_json_4.json', 'w')


	for filename in os.listdir(path_read):
		print filename
		try:
			if filename.endswith('.json'): 
				read_file = open(path_read+'/'+filename, 'r').readlines()
				twit_list = json_output(read_file) # return a list 
				features = features + twit_list
		except:
			os.remove(path_read+'/'+filename)
	#print len(features)
	json_out_1["features"] = features[0:175000]
	json_out_2["features"] = features[175000:350000]
	json_out_3["features"] = features[350000:525000]
	json_out_4["features"] = features[525000:len(features)]


	geo_json_dump_1 = json.dumps(json_out_1, indent=4)
	geo_json_dump_2 = json.dumps(json_out_2, indent=4)
	geo_json_dump_3 = json.dumps(json_out_3, indent=4)
	geo_json_dump_4 = json.dumps(json_out_4, indent=4)
	#print >> one_json, "eqfeed_callback("
	print >> one_json_1, geo_json_dump_1
	print >> one_json_2, geo_json_dump_2
	print >> one_json_3, geo_json_dump_3
	print >> one_json_4, geo_json_dump_4
	#print >> one_json, ")"
	one_json_1.close()
	one_json_2.close()
	one_json_3.close()
	one_json_4.close()
	
main()



