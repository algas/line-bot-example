import http.client
import urllib.parse
import json
import os

class LineClient(object):
    def __init__(self, config):
        self.config = config

    def content_text(self, text):
        return  { "contentType": 1,
                  "toType": 1,
                  "text": text
                }

    def content_image(self, image_url, thumbnail_url=None):
        return  { "contentType": 2,
                  "toType": 1,
                  "originalContentUrl": image_url,
                  "previewImageUrl": thumbnail_url or image_url
                }

    def events(self, users, content):
        query = { 'to': users,
                  'toChannel': 1383378250,
                  'eventType':'138311608800106203',
                  'content': content
                }
        params = json.dumps(query, ensure_ascii=False)
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'X-Line-ChannelID': self.config['CHANNEL_ID'],
                   'X-Line-ChannelSecret': self.config['CHANNEL_SECRET'],
                   'X-Line-Trusted-User-With-ACL': self.config['PROVIDER_MID']}
        conn = http.client.HTTPSConnection(self.config['API_HOST'])
        conn.request('POST', '/v1/events', params, headers)
        res = conn.getresponse()
        conn.close()
        return res
