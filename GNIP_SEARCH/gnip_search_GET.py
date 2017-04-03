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


class RequestWithMethod(urllib2.Request):
    def __init__(self, url, method, headers={}):
        self._method = method
        urllib2.Request.__init__(self, url, headers)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)

if __name__ == "__main__":

	url = GNIP_URL
	UN = GNIP_UN
	PWD = GNIP_PWD
	query = 'hiring :has_links'

	queryString = url + '?publisher=twitter&query=' + query

	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')

	req = RequestWithMethod(queryString, 'GET')
	req.add_header("Authorization", "Basic %s" % base64string)

	try:
		response = urllib2.urlopen(req) #KEEP GETTING ERROR HERE!
	except urllib2.HTTPError as e:
        	print e.read()

	the_page = response.read() #AND HERE!
	print the_page
