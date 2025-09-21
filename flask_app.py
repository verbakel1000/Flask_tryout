import flask from flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>Hello World! Huiswerk les 11 klaar :)<p>"
