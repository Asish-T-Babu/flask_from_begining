from flask import Flask, request, make_response

app = Flask(__name__)

# Here we are passing the status code as the second argument for the return 
@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello world</h1>", 200

@app.route('/hello', methods=['GET', 'POST']) # interroute defenition -> this means we need to specify the allowed request methods in the route itself, other methods are not allowed in method lis in url and by default every url is in GET method 
def hello():
    # return 'Hello world'
    # here instead of returnig the above response and status code we can create a response using make_response, so we can specify the application type, status code and teh value
    response = make_response('Hello world')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response

# Dynamic Url Creation
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

# here the teacher is trying to say, the values passed using url will by default string and we need to type cast it for the calculation but we can directly typecast it usig the url itself
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return {"sum":number1+number2}

@app.route('/handle_url_params')
def hanle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"
    return "Some parameters are missing"

# How to differentiate multiple url methods in one route
@app.route('/request_type', methods = ['GET', 'POST'])
def request_type():
    if request.method == 'GET':
        return 'You made a GET request'
    if request.method == 'POST':
        return 'You made a POST request'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug= True)
