from flask import Blueprint
from flask import render_template, redirect, url_for

routes = Blueprint('routes',__name__,url_prefix='',template_folder='templates',static_folder='static')

# Registration routes moved to app.py to avoid conflicts
# and consolidate registration logic



    
