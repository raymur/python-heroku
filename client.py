#!/usr/bin/env python
from flask import Flask
import urllib3
import json

application = Flask(__name__)
import os
port = os.environ['SERVER_PORT']

proxy = urllib3.ProxyManager("http://127.0.0.1:%s" % port)


@application.route("/")
def hello_world():
    response =  proxy.request("GET", '/name')
    response_data = json.loads(response.data)
    name = response_data.get('name')
    return "<p>Hello, %s!</p>" % name

