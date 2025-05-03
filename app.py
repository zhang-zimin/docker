from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response('Hello from Docker!')
    response.headers['X-Served-By'] = 'Flask'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 