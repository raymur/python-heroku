#!/usr/bin/env python
from flask import Flask
import urllib3
import json

application = Flask(__name__)

@application.route("/")
def hello_world():
    response =  urllib3.request("GET", "127.0.0.1:8001")
    response_data = json.loads(response.data)
    name = response_data.get('name')
    return "<p>Hello, %s!</p>" % name

