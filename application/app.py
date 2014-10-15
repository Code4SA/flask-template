from flask import Flask, url_for
import os

app = Flask(__name__)

env = os.environ.get('FLASK_ENV', 'development')
app.config['ENV'] = env

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

# setup assets
from flask.ext.assets import Environment, Bundle
from .app import app

assets = Environment(app)
assets.url_expire = False
assets.debug      = app.config['ENV'] == 'development'
assets.load_path  = ['%s/assets' % app.config.root_path]

assets.register('css',
    Bundle(
      'stylesheets/**/*.css',
      Bundle(
        'stylesheets/*.scss',
        filters='pyscss',
        output='stylesheets/app.%(version)s.css'),
      output='stylesheets/all.%(version)s.css'))

assets.register('js', Bundle(
    'js/**/*.js',
    output='js/app.%(version)s.js'))

from . import views
