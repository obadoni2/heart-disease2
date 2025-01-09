from flask import Blueprint
from flask import render_template, redirect, url_for

routes = Blueprint('routes',__name__,url_prefix='',template_folder='templates',static_folder='static')

# Registration routes moved to app.py to avoid conflicts
# and consolidate registration logic



@routes.route('/patregis')
def patregis():
    return render_template('patregis.html')


@routes.route('/docregis')
def docregis():
    return render_template('docregis.html')

    
