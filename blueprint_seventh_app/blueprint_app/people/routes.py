from flask import request, render_template, redirect, url_for, Blueprint

from blueprint_app.app import db
from blueprint_app.people.models import Person

people = Blueprint('people', __name__, template_folder='templates')

@people.route('/')
def index():
    peoples = Person.query.all()
    return render_template('people/index.html', peoples= peoples)

@people.route('/create', methods= ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('people/create.html')
    elif request.method == "POST":
        name = request.form.get('name')
        age = int(request.form.get('age'))
        job = request.form.get('job')
        person = Person(name=name, age=age, job=job)
        # done = True if 'done' in request.form.key() else False
        person= Person(name= name, age= age, job= job)
        db.session.add(person)
        db.session.commit()

        return redirect(url_for('people.index'))