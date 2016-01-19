#!/usr/bin/env python2

import argparse
import urllib
import urllib2
import urlparse
import base64
import json
import sys

parser = argparse.ArgumentParser(description='Obtain access token from Twitter')

parser.add_argument('-c', '--consumer-key', action='store', dest='consumer_key', help='Consumer key')
parser.add_argument('-s', '--consumer-secret', action='store', dest='consumer_secret', help='Consumer key')
parser.add_argument('-u', '--api-url', action='store', dest='api_url', help='API URL',
                    default='https://api.twitter.com')

if len(sys.argv) == 1:
    sys.argv.append('--help')

args = parser.parse_args()

if not args.consumer_key or not args.consumer_secret:
    parser.error('Consumer key and consumer secret required')
    exit()

auth_header = 'Basic %s' % base64.urlsafe_b64encode('%s:%s' % (args.consumer_key, args.consumer_secret))

url = urlparse.urljoin(args.api_url, 'oauth2/token')
req = urllib2.Request(url, data=urllib.urlencode({'grant_type': 'client_credentials'}),
                      headers={'Authorization': auth_header})
access_token = json.load(urllib2.urlopen(req))['access_token']

with open('.twitter_token', 'w') as f:
    f.write(access_token)

print 'Now you can use other twitter scripts.'
