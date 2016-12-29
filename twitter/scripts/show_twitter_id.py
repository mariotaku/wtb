#!/usr/bin/env python2

import argparse
import json
import re
import urllib
import urllib2
import urlparse
import sys

if len(sys.argv) == 1:
    sys.argv.append('--help')

token = None

with open('.twitter_token') as f:
    token = f.readline()

if not token:
    print 'No token, use obtain_token first'
    exit()

parser = argparse.ArgumentParser(description='Show user ID corresponding to @screenname or url')

parser.add_argument('name_or_url', help='@screenname or url')
parser.add_argument('-u', '--api-url', action='store', dest='api_url', help='API URL',
                    default='https://api.twitter.com')

args = parser.parse_args()

screen_name = None

m = re.match('^((https?://)?(www\.)?twitter\.com/)?(@|#!/)?([A-Za-z0-9_]{1,15})(/([-a-z]{1,20}))?$', args.name_or_url)
if m:
    screen_name = m.group(5)
else:
    print 'Invalid name or url'
    exit()

auth_header = 'Bearer %s' % token

url = urlparse.urljoin(args.api_url, '1.1/users/show.json?%s' % urllib.urlencode({'screen_name': screen_name}))
req = urllib2.Request(url, headers={'Authorization': auth_header})

user = json.load(urllib2.urlopen(req))

print user['id_str']
