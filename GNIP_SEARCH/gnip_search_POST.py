#!/usr/bin/env python

import ConfigParser
import urllib2
import base64
import json
import xml
import sys


# Read config file to access API keys
cfg = ConfigParser.ConfigParser()
cfg.read('../config.ini')
GNIP_URL = cfg.get('GNIP_KEYS','api_url')
GNIP_UN = cfg.get('GNIP_KEYS','api_un')
GNIP_PWD = cfg.get('GNIP_KEYS','api_pwd')


def post():

	url = GNIP_URL
	UN = GNIP_UN
	PWD = GNIP_PWD

	rule = 'hiring :has_links'

	query = '{"query":"' + rule + '","publisher":"twitter"}'


	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')
	req = urllib2.Request(url=url, data=query)
	req.add_header('Content-type', 'application/json')
	req.add_header("Authorization", "Basic %s" % base64string)


	try:
		response = urllib2.urlopen(req) #KEEP GETTING ERROR HERE!
	except urllib2.HTTPError as e:
		print e.read()
	the_page = response.read() #AND HERE!
	print the_page

if __name__ == "__main__":
        post()
