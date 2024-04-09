from flask import render_template, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required

from models import Person, Users

def register_routes(app, db, bcrypt):
    
    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')
            person = Person(name=name, age=age, job=job)
            db.session.add(person)
            db.session.commit()
            people = Person.query.all()
            return render_template('index.html', people = people)
        if request.method == "GET":
            people = Person.query.all()
            return render_template('index.html', people = people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        return jsonify({'status': 'success', 'data':'Person deleted successfully'}), 200

    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template('detail.html', person= person)
    
    @app.route('/home', methods=['GET', 'POST'])
    def home():
        return render_template('user_authentication/index.html')
    
    @app.route('/login/<uid>')
    def user_login(uid):
        user = Users.query.get(uid)
        login_user(user)
        return 'Success'    @app.route('/login/<uid>')
    
    app.route('/logout')
    def user_login():
        login_user()
        return 'Success'