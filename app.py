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
    response.headers['Etag'] = "21ry8f392h93"
    response.cache_control.max_age = 15
    return response

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response


if __name__ == "__main__":

    #app.run(debug=True, port=8001, threaded=True)
    app.run(port=8001, threaded=True)
