# Import libraries
import flask


# Create a variable named app
app = flask.Flask(__name__) 


# Reponse for resquests
@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    output = next(flask.request.form.values())
    return flask.render_template('index.html', prediction_text=output)


# Entry point
if __name__ == '__main__':
    app.run()