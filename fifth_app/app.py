from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Asish'
    session['other'] = 'Hello World'
    print('hello')
    return render_template('index.html', message= 'session data set')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message= f"Name: {name}, Other: {other} from get data")
    else:
        return render_template('index.html', message = f"Session data not found")

@app.route('/clear_session')
def clear_session():
    
    if 'name' in session.keys() and 'other' in session.keys():
        # session.clear() # Here all the session in our project will be cleared using clear()
        session.pop('name') # clear particular session from the project
        session.pop('other')
        return render_template('index.html', message = 'Session cleared')
    else:
        return render_template('index.html', message = f"Session data not found")

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message = cookie_value)

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie removed'))
    response.set_cookie('cookie_name', expires=0)
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "asish" and password == '12345':
            flash('Successfull login')
            return render_template('index.html', message= '')
        else:
            flash('Login failed')
            return render_template('index.html', message= '')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug= True)