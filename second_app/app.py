from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # Passing value to the template
    return render_template('index.html', myname = 'Asish', greetings = 'Hello', list1 = [1, 2, 3, 4, 5], some_text = 'Hello World')

# Dynamic URL -> This can be achieved using url_for('<fuction_name>') in the template or in the function we need to redirect. we don't need to specify the exact url instead of that we can use the function name associate with the url, where we need to give the url 
@app.route('/href_without_url')
def url_func():
    return render_template('dynamic_url.html')

# Redirect to some other url
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('index'))

# Template filter -> by default the jinja is giving some filters like | upper, | lower, etc .. now we are going to create custom filter
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')