from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/hello", code=302)

@app.route('/hello')
def hello_world():
    data = {'message': 'Hello, World!'}
    response = jsonify(data)
    return response


@app.route('/cached_hello')
def cacheable_hello_world():
    data = {'message': 'Hello, World! This can be cached for 15 secs.'}
    response = jsonify(data)
    response.cache_control.max_age = 15
    return response


@app.route('/version')
def get_version():

    version = ""
    with open("VERSION", 'r') as fd:
        version = fd.read().strip()

    data = {'version': version}
    response = jsonify(data)
    return response


@app.route('/name')
def get_name():

    name = ""
    with open("NAME", 'r') as fd:
        name = fd.read().strip()

    data = {'name': name}
    response = jsonify(data)
    return response


@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response


if __name__ == "__main__":

    #app.run(debug=True, port=9902, threaded=True)
    app.run(port=9902, threaded=True)
