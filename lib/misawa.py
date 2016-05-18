# -*- coding: utf-8 -*-
import http.client
import urllib.parse
import json
import random
import sys
import logging

def client():
    conn = http.client.HTTPConnection("horesase.github.io")
    conn.request('GET', '/horesase-boys/meigens.json')
    res = conn.getresponse()
    status = res.status
    body = res.read()
    js = json.loads(body.decode('utf-8'), 'utf-8')
    conn.close()
    return js

def client_dic():
    js = client()
    dic = {}
    return {j['title']+j['body']:j['image'] for j in js if 'title' in j and 'body' in j and 'image' in j}

def random_misawa(key):
    tbl = client_dic()
    logging.info(key)
    for k, v in tbl.items():
        if key in k:
            logging.info(k)
            return v
    logging.info("at random")
    return tbl[random.choice(list(tbl.keys()))]
        
if __name__ == '__main__':
    k = sys.argv[1]
    print(random_misawa(k))

