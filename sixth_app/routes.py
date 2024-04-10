from flask import render_template, request, jsonify, redirect, url_for
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
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('home'))
    
    @app.route('/signup', methods=['GET','POST'])
    def signup():
        if request.method == 'GET':
            return render_template('user_authentication/signup.html')
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            hash_password = bcrypt.generate_password_hash(password)
            user = Users(username=username, password= hash_password, role='user')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))


    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('user_authentication/login.html')
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            user = Users.query.filter_by(username=username).first()
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                return 'Failed'
    

    @app.route("/secret")
    @login_required
    def secret():
        if current_user.role == 'admin':
            return 'My secret Message'
        else:
            return 'No permission required'
    
    