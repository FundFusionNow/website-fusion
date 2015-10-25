import flask
import urllib2
import re
import time
from google.appengine.ext import db

app = flask.Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
