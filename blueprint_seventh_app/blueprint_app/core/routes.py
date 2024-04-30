from flask import request, render_template, Blueprint

from blueprint_app.app import db

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def index():
    return render_template('core/index.html')
