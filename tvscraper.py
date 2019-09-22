from urllib import request
from bs4 import BeautifulSoup as Soup
import vlc
import time
import os
from threading import Thread
import json
from fake_useragent import UserAgent

class tvscraper():
    def __init__(self):
        self.channel_dict = self.get_channels()
        self.agents = UserAgent()

    def get_channels_dict(self):
        return self.channel_dict
    
    def get_channels(self, channelpath='channels.json'):
        assert os.path.exists(channelpath), "No channel configuration file path exists"
        with open(channelpath, 'r') as file:
            return json.load(file)['channels']

    def get_stream_link(self, channel):
        if not (channel in self.channel_dict):
            return {'code': 403, 'msg': 'invalid channel name'}
        req = request.Request(
            self.channel_dict[channel.lower()],
            headers={
                'User-Agent': self.agents.random
            }
        )
        try:
            response = request.urlopen(req)
            soup = Soup(response, 'html.parser')
            streamlink = bsoup.findAll("script")[15].next_element.split(" file: ")[1].split(',')[0].strip("\'")
            return {'code': 200, 'msg': streamlink}
        except:
            return {'code': 403, 'msg': 'Internal error occured'}
