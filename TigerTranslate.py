import flask
from flask import request
from flask import json
from flask_cors import CORS

# create a variable named app
app = flask.Flask(__name__) 
CORS(app)

# function predict is called at each request  
@app.route("/predict", methods=["POST"])
def predict():
    print(request.data)

    response = {"output": 'cat'}
    return flask.jsonify(response) # return it as json


if __name__ == '__main__':
    app.run(host='0.0.0.0')