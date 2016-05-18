# -*- coding: utf-8 -*-
from bottle import get, post, route, run, template, request, response
import http.client
import urllib.parse
import json
import os
import lib.misawa
import lib.lineclient
import logging

@get('/')
def index():
    return 'hello'

@get('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@post('/callback')
def cbk():
    data = request.json
    _from = ""
    _text = ""
    for k,v in data['result'][0].items():
        if k == 'content':
            _from = v['from']
            _text = v['text']
    image_url = lib.misawa.random_misawa(_text)
    logging.info(image_url)
    client = lib.lineclient.LineClient(os.environ)
    users = [_from]
    content = client.content_image(image_url)
    res = client.events(users, content)
    status = res.status
    body = res.read()
    logging.info(status)
    return template('{{status}}', status=status)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%D', level=logging.INFO)
    run(host='0.0.0.0', port=5000)
