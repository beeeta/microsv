#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by betalun on 4/26/17
from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

# if __name__ == '__main__':
#     run_simple('localhost', 5000, app,
#                use_reloader=True, use_debugger=True, use_evalex=True)

from werkzeug.wsgi import DispatcherMiddleware


application = DispatcherMiddleware(app)
