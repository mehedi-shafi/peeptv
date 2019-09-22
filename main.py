import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from flask import jsonify

from tvscraper import tvscraper

tvbox = tvscraper()

@app.route('/stream-link/<channel_name>')
def get_channel_stream_link(channel_name):
    stream_link = tvbox.get_stream_link(channel_name)
    return jsonify(stream_link)

@app.route('/channel_list', methods=['GET'])
def get_channel_list():
    return jsonify(tvbox.get_channels_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
