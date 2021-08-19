#!/usr/bin/env python3

import json
import requests
import threading

url = 'https://radar.somoynews.tv/graphql'

headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}


rdata = requests.post(url, data=open('payload.json', 'rb'), headers=headers)
j = json.loads(rdata.text)

print(j)

print(j['data']['updatePoll']['id'] + " : " + j['data']['updatePoll']['options'][0] + " votes.")



