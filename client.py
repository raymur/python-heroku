#!/usr/bin/env python
from flask import Flask
import urllib3
import json

application = Flask(__name__)
import os
port = os.environ['SERVER_PORT']


@application.route("/")
def hello_world():
    response =  urllib3.request("GET", "0.0.0.0:%s" % port)
    response_data = json.loads(response.data)
    name = response_data.get('name')
    return "<p>Hello, %s!</p>" % name

