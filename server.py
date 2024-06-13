#!/usr/bin/env python
from flask import Flask

application = Flask(__name__)

@application.route("/name")
def root():
    return '{"name": "ray"}'
