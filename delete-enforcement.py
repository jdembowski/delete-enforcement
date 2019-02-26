#!/usr/bin/python3

import requests, json, sys

# From https://docs.umbrella.com/enforcement-api/reference/#domain2

# curl -v \
#		 -H 'Content-Type: application/json' \
#		 -X DELETE 'https://s-platform.api.opendns.com/1.0/domains/domaintodelete.com?customerKey=XXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' -v -X DELETE

# Deleting entries from an Enforcement API in bulk is time consuming as the deletion is one domain at a time.

# Read API token
with open('enforcement-api-key.txt', 'r') as k:
    api_key = k.read().rstrip()

# Domains to delete are in a text file one domain at a time. Thia script takes
# that file and reads it like so.
#
# example1.com
# example2.com
# example3.net
# example4.net
# example5.org

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print('ERROR: please provide an input file name')
    sys.exit(1)

with open(filename) as f:
    domains = f.read().splitlines()

domain=[]

for domain in domains:

    method='DELETE'
    headers = {'content-type': 'application/json'}
    req = requests.request(method, 'https://s-platform.api.opendns.com/1.0/domains/'+domain+'?customerKey='+api_key, headers=headers)
    response=req.status_code

    # A 204 code means the DELETE was successful.
    # A 404 means the DELETE failed as the entry was not found.
    print('Domain:', domain, 'Response code:', response, flush=True)
