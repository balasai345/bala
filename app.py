# app.py
from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return "Hello, World! This is a Flask app running in Docker."

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
