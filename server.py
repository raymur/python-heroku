#!/usr/bin/env python
from flask import Flask

application = Flask(__name__)

@application.route("/")
def root():
    return '{"name": "ray"}'
