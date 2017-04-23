import json
import unicodedata
import os


def json_output(input_file):
	json_out ={}
	features = []

	Type = {}
	Type["type"] = "FeatureCollection"
	json_out.update(Type)

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
				#if lng > 0:
				#	lng = float( items['geo']['coordinates'][1])
				#	lat = float (items['geo']['coordinates'][0])
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
	return json_out


def main():
	path_read 	= 	'/home/user/Dropbox/CU/ATLS_5214/project/DataDreamTeam/shineynewset/'
	path_write 	= 	'/home/user/Dropbox/CU/ATLS_5214/project/DataDreamTeam/geo_jsons_twits/'
	for filename in os.listdir(path_read):
		if filename.endswith('.json'): 
			read_file = open(path_read+'/'+filename, 'r').readlines()
			write_file = open(path_write+'/'+filename,'w')
			geo_json = json_output(read_file)
			geo_json_dump = json.dumps(geo_json, indent=4)
			print >> write_file, geo_json
			#read_file.close()
			write_file.close()
			
main()


