import flask from flask

@app.route('/')
def home():
    return "Hello World"
